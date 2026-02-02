import os
import requests
import difflib
import zipfile
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# 1. SETUP & CONFIGURATION
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
BACKUP_DIR = REPO_ROOT / "backups"

load_dotenv(REPO_ROOT / ".env")
DUET_HOST = os.getenv("DUET_HOST")

TARGET_FOLDERS = ["sys", "macros"]

def get_url(endpoint, params=""):
    return f"http://{DUET_HOST}/{endpoint}?{params}"

# 2. CORE LOGIC FUNCTIONS

def backup_machine():
    """Captures the current state of the Duet into a ZIP file."""
    if not DUET_HOST: return
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    BACKUP_DIR.mkdir(exist_ok=True)
    zip_filename = f"duet_backup_{timestamp}.zip"
    zip_path = BACKUP_DIR / zip_filename
    
    print(f"\n[!] Creating remote backup: {zip_filename}")
    try:
        with zipfile.ZipFile(zip_path, 'w') as backup_zip:
            for folder in TARGET_FOLDERS:
                r = requests.get(get_url("rr_filelist", f"dir=0:/{folder}"), timeout=10)
                if r.status_code == 200:
                    for f_info in r.json().get('files', []):
                        fname = f_info['name']
                        # Use .content (raw bytes) to avoid newline translation
                        f_resp = requests.get(get_url("rr_download", f"name=0:/{folder}/{fname}"))
                        backup_zip.writestr(f"{folder}/{fname}", f_resp.content)
        print("✓ Backup complete.")
        return True
    except Exception as e:
        print(f"FAILED to backup: {e}")
        return False

def check_drift(silent=False):
    """Symmetric comparison with newline-insensitive logic."""
    if not silent:
        print(f"\n--- Checking Drift (Machine: {DUET_HOST}) ---")
    
    orphans, staged, modified = [], [], []

    for folder in TARGET_FOLDERS:
        local_folder = REPO_ROOT / folder
        local_files = {f.name for f in local_folder.glob('*.[gc]*')}
        
        try:
            r = requests.get(get_url("rr_filelist", f"dir=0:/{folder}"), timeout=10)
            if r.status_code == 200:
                remote_files = {f['name'] for f in r.json().get('files', []) if f['type'] == 'f'}
            else: continue
        except Exception: continue

        for f in (local_files - remote_files):
            staged.append((folder, f))
            if not silent: print(f"[STAGED] {folder}/{f} (Local only)")

        for f in (remote_files - local_files):
            orphans.append((folder, f))
            if not silent: print(f"[ORPHAN] {folder}/{f} (Machine only)")

        for f in (local_files & remote_files):
            resp = requests.get(get_url("rr_download", f"name=0:/{folder}/{f}"))
            if resp.status_code == 200:
                # Read local using 'newline=""' to prevent Windows from altering \n
                with open(local_folder / f, 'r', encoding='utf-8', newline='') as lf:
                    local_text = lf.read().splitlines()
                
                # Use .text.splitlines() for comparison (splitlines is newline-agnostic)
                remote_text = resp.text.splitlines()
                
                if local_text != remote_text:
                    modified.append((folder, f))
                    if not silent:
                        print(f"⚠ DRIFT: {folder}/{f}")
                        for line in difflib.unified_diff(remote_text, local_text, n=0):
                            if line.startswith(('+', '-')) and not line.startswith(('+++', '---')):
                                print(f"    {line}")

    if not silent and not (orphans or staged or modified):
        print("✓ Everything is in sync.")
    
    return orphans, staged, modified

def push_to_machine():
    """Deploy Git version to the Machine."""
    check_drift()
    confirm = input("\nOVERWRITE Machine with Git files? (y/n): ")
    if confirm.lower() != 'y': return

    if backup_machine():
        for folder in TARGET_FOLDERS:
            for local_file in (REPO_ROOT / folder).glob('*.[gc]*'):
                # Read raw bytes to preserve exact file structure
                with open(local_file, 'rb') as f:
                    requests.post(get_url("rr_upload", f"name=0:/{folder}/{local_file.name}"), data=f)
                print(f"  Pushed: {local_file.name}")
        print("✓ Push complete.")

def pull_from_machine():
    """Accept Machine version as Source of Truth, preserving Unix line endings."""
    orphans, staged, modified = check_drift(silent=False)
    
    to_pull = orphans + modified
    if not to_pull:
        print("\nNothing to pull.")
        return

    print(f"\nFound {len(to_pull)} items to pull.")
    confirm = input("OVERWRITE Local Git files with Machine versions? (y/n): ")
    if confirm.lower() != 'y': return

    for folder, name in to_pull:
        resp = requests.get(get_url("rr_download", f"name=0:/{folder}/{name}"))
        if resp.status_code == 200:
            local_path = REPO_ROOT / folder / name
            local_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Use binary write mode ('wb') to save the exact bytes from the Duet
            # This prevents Windows from adding extra \r characters.
            with open(local_path, 'wb') as f:
                f.write(resp.content)
            print(f"  Pulled: {folder}/{name}")
    print("✓ Pull complete.")

# 3. INTERFACE (Standard Menu)
def main_menu():
    while True:
        print("\n" + "="*45)
        print(f" DUET 3 MB6HC MANAGER | HOST: {DUET_HOST}")
        print("="*45)
        print("1. [D]rift Check")
        print("2. [B]ackup Machine")
        print("3. [P]ush to Machine")
        print("4. [L]oad from Machine")
        print("5. [E]xit")
        
        choice = input("\nSelection: ").strip().lower()
        if choice in ['1', 'd']: check_drift()
        elif choice in ['2', 'b']: backup_machine()
        elif choice in ['3', 'p']: push_to_machine()
        elif choice in ['4', 'l']: pull_from_machine()
        elif choice in ['5', 'e']: sys.exit()

if __name__ == "__main__":
    if not DUET_HOST:
        print("ERROR: DUET_HOST not found.")
    else:
        try:
            main_menu()
        except KeyboardInterrupt:
            sys.exit()