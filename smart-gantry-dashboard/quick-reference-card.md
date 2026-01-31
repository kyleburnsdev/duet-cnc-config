# 🐝 Ultimate Bee: Smart Gantry Quick Reference

## 1. The Dashboard Zones

The gantry light is divided into three functional areas. Use these to monitor the machine from across the room.

* **LEFT (Status):** Tells you **HOW** the machine is feeling (Health/Mode).
* **CENTER (Center):** Illuminates **WHAT** the machine is doing (Work Area).
* **RIGHT (Progress):** Shows **WHEN** the machine will be finished (Timeline).

---

## 2. Status Color Code (Left Side)

| Color | Pattern | Meaning | Action Required |
| --- | --- | --- | --- |
| **Amber** | Solid (Dim) | **Standby** | None; machine is idle and safe. |
| **Green** | Solid | **Running** | None; machine is operating normally. |
| **Blue** | Solid | **Probing** | Ensure probe is attached and clear. |
| **Yellow** | Solid | **Paused** | Machine is waiting for a command or check. |
| **Magenta** | **Pulsing** | **Tool Change** | **Manual bit change required.** |
| **Red** | **FLASHING** | **FAULT / HALT** | **Check for E-Stop, limit hit, or error.** |

---

## 3. Progress Monitoring (Right Side)

The right-hand gauge represents 0% to 100% of the current file.

* **Filling Blue:** Represents completed work.
* **Increasing Brightness:** The single "active" light will slowly get brighter as it fills its 5% bucket, indicating the machine has not hung.
* **Dim Track:** A very faint blue line shows the total length of the gauge for reference.

---

## 4. Task Lighting (Center)

* **Bright White:** Automatically triggers during a job for maximum visibility of the cut.
* **Soft White:** Automatically triggers when idle to act as ambient shop lighting without glare.
* **Green Flash:** When the Z-probe touches the plate, the entire gantry flashes Green once to confirm the "Zero" was captured.

---

### Operator Pro-Tip

> **"If it's Magenta, it needs a bit. If it's Red, it's hit a quit."**
> Use the sub-pixel brightness on the right to gauge if your feed rate is effective; if the light is barely getting brighter over several minutes, you may want to check your total estimated time remaining in the Duet Web Control.
