# `/maintenance_scripts/` README.md

This directory contains the Python-based utilities for managing the **Duet 3 MB6HC** configuration, detecting "live" machine changes, and performing safety backups.

## 🛠 Prerequisites

Before running the scripts, ensure your local environment is configured:

1. **Python 3.10+** installed.
2. **Virtual Environment** active:
```bash
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

3. **Dependencies** installed:
```bash
pip install -r ../requirements.txt

```

## 🌐 Configuration (`.env`)

The scripts pull the machine's network address from a `.env` file located in the project root. This file is excluded from Git for security.

**Required Entry:**

```text
DUET_HOST=192.168.1.XX  # Replace with your actual Duet IP

```

---

## 🚀 The Manager Script: `duet_manager.py`

This is the primary interface for machine maintenance. It can be executed from the project root:

```bash
python maintenance_scripts/duet_manager.py

```

### Main Menu Actions:

1. **Check for Configuration Drift**
* Downloads the current files from the Duet's SD card.
* Performs a `unified_diff` against the local `/sys/` and `/macros/` folders.
* **Use Case:** Run this before starting a session to see if you made any "quick tweaks" at the machine console that haven't been committed to Git yet.

2. **Run Full Machine Backup**
* Recursively crawls the machine's `/sys/` and `/macros/` directories.
* Packages all current files into a timestamped `.zip` in the `/backups/` folder.
* **Use Case:** Before making major hardware changes or firmware updates.

3. **Push Git Configuration to Machine**
* **Safety First:** This automatically triggers a backup before proceeding.
* Overwrites the machine's SD card with the current state of your local Git repository.
* **Use Case:** Deploying new macros or updated motor/tuning settings.

---

## 📂 Standard File Structure

The scripts expect the following layout relative to the repository root:

* `/sys/`: Core RRF configuration (`config.g`, `homeall.g`, etc.)
* `/macros/`: Custom CNC utilities (Probing, Framing, Spindle Warm-up)
* `/backups/`: Destination for automated ZIP snapshots (Tracked in Git)

---

## ⚠️ Safety Warnings

* **M999:** After pushing a new configuration, the Duet must be restarted to apply changes to the Object Model. Send `M999` via the Duet Web Control (DWC) console or the physical reset button.
* **Partial Uploads:** While the script includes error handling, always verify the DWC console for any "File Not Found" errors after a push, especially if the WiFi connection is weak.
* **Git Merges:** Never push a file that has unresolved Git merge markers (`<<<<<<< HEAD`). The Duet will attempt to execute them as G-Code, leading to unpredictable behavior.
