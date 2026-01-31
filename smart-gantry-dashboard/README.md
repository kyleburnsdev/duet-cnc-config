# Functional Specification: Smart Gantry Dashboard UX

**Project Scope:** Integrated Peripheral Awareness System

**Hardware Platform:** Ultimate Bee 1500mm CNC

## 1. Design Philosophy

The Smart Gantry Dashboard replaces traditional "status LEDs" with a 1-meter linear information display. The goal is to maximize **"Glanceable Data"**—allowing the operator to understand the machine’s health, progress, and needs from anywhere in the shop via peripheral vision.

---

## 2. Spatial Architecture (The Three-Zone Layout)

The gantry is divided into three logical zones to create a consistent spatial map for the operator’s eye.

### Zone A: The "Andon" Status Tower (Left Side)

Located at the machine's "Home" side, this zone communicates the **Machine State**. It mimics industrial stack lights found in high-end manufacturing.

* **Why:** It provides a singular "health check" point. By keeping it on the left, the operator instinctively knows that the "Origin" of the machine is the source of truth for its current status.

### Zone B: Active Task Lighting (Center)

The longest section of the strip, focused directly over the spindle and work area.

* **Why:** To provide shadow-free, high-CRI illumination during the cut. It dynamically shifts intensity based on whether the machine is active, reducing eye strain during setup and maximizing visibility during operation.

### Zone C: High-Resolution Progress Gauge (Right Side)

A linear bar that fills from left to right as the job progresses.

* **Why:** Humans process linear spatial progress more intuitively than numeric percentages. By placing this on the far right, it serves as a "Timeline" for the machine's activity.

---

## 3. Visual Communication Language

### 3.1 Operational States

* **Standby (Warm Amber):** Indicates the machine is powered and safe to approach, but currently idle. The warm tone distinguishes it from the clinical white used during work.
* **Healthy Processing (Solid Green + Bright White):** The "All Systems Go" state. Green status confirms the controller is happy; bright center lighting ensures the tool-path is visible.
* **Paused (Solid Yellow):** Indicates a non-critical halt. The machine is waiting for user input (such as a door close or a manual check) to continue.

### 3.2 High-Priority Alerts

* **Tool Change Required (Pulsing Magenta):** A high-visibility, distinct color used to demand operator intervention. Magenta is used because it rarely occurs in nature or standard shop environments, making it immediately recognizable as an "action required" signal.
* **Emergency / Fault (Flashing Red):** A rhythmic, high-contrast flash. This is designed to trigger a biological "danger" response in the peripheral vision, ensuring the operator notices a stall, limit-switch hit, or E-stop even if they are wearing hearing protection or looking elsewhere.

### 3.3 Tactile Feedback (Probing)

* **Active Seek (Solid Blue):** Confirms the machine has entered "Sensing Mode."
* **Contact Confirmation (Flash Green):** Provides immediate visual "Success" feedback the instant the electrical circuit is closed. This prevents the operator from second-guessing if the "Zero" was actually captured.

---

## 4. Advanced Progress Visualization

The dashboard utilizes **Sub-Pixel Interpolation**. Unlike traditional bars that jump from one LED to the next, the "active" LED in the progress zone slowly increases in brightness.

* **The Benefit:** This eliminates the "frozen" feeling of long CNC jobs. On a 20-minute cut, a standard LED bar might not move for a full minute. With sub-pixel fading, the operator can see the machine is making progress second-by-second, providing continuous reassurance.

---

## 5. Environmental Adaptation

* **Dim-on-Idle:** To prevent the machine from becoming a source of light pollution in the shop or burning out LEDs prematurely, the system automatically dims the task lighting when the machine is not actively running a job.
* **Glare Mitigation:** The system caps peak brightness to prevent harsh reflections off aluminum extrusions or shiny work materials, ensuring the UX aids visibility rather than hindering it.
