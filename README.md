# Duet3D 6HC CNC Build

The project is to plan and document set-up and configuration of a hobby CNC machine based around a Bulkman3D Ultimate Bee 1500 x 1500 CNC and Duet3D 6HC controller

## Main System Components

This section describes the major components that form the foundation for the build

### Ultimate Bee CNC

The Bulkman3D Ultimate Bee 1500 x 1500 CNC represents the mechanical foundation of this hobby CNC build. This robust machine offers a spacious work area of 1500mm x 1500mm, providing ample room for various CNC projects and materials. The frame is constructed with high-quality aluminum extrusions and steel components, ensuring durability and stability during operation.

The Ultimate Bee design has its roots in the popular OpenBuild CNC platform, which provided a foundation for open-source CNC machine development. Bulkman3D has enhanced this design with their own improvements while maintaining compatibility with many of the original OpenBuild components and principles.

Key characteristics include:

- **Work Area**: 1500mm x 1500mm (59" x 59")
- **Travel Distance**: X-axis: 1500mm, Y-axis: 1500mm, Z-axis: 150mm
- **Construction**: Aluminum extrusion frame with steel structural components
- **Precision**: High-precision ball screws and linear bearings for smooth operation
- **Motor Mounting**: Pre-drilled and tapped mounting points for standard stepper motors
- **Spindle Holder**: Compatible with various spindle configurations
- **Spindle**: 2.2kW air-cooled spindle
  - Rated Power: 2.2kW
  - Speed Range: Typically 0-24,000 RPM (verify with spindle specs)
  - Cooling: Air-cooled
- **VFD**: Huanyang HY02D211B
  - Model: HY02D211B (2.2kW, single-phase input)
  - Input: 110V single-phase
  - Output: 220V 3-phase
  - Rated Current: ~10A output
  - Control: RS-485 (Modbus RTU protocol)
  - Features: Variable frequency 0-400Hz, overload protection
- **Limit Switches**: 24V inductive proximity sensors (LJ12A3-4-Z/AX)
  - Type: PNP inductive
  - Voltage: 24V DC

This CNC machine provides an excellent platform for hobbyists and makers seeking a reliable, scalable solution for their CNC projects. Its modular design allows for future upgrades and customizations while maintaining the structural integrity necessary for precision machining.

### NEMA 23 High Torque Stepper Motor

This High Torque NEMA23 stepper motor is a great choice for any project that requires more power and more strength. With a holding torque of 2.45N.m (346oz.in) they are a great addition for larger machines requiring higher torque.

They come with a 150mm lead with a EDG-4P.

#### Wiring Details

- A+ - Red
- A- - Green
- B+ - Blue
- B- - Yellow

#### Operating characteristics

- Step Angle：1.8°
- Rated current：3.0A DC
- Rated Voltage: 3.6V
- Winding dc resistance (25℃): 1.2Ω±10%
- Winding inductance: 4mH±20%
- Holding torque：≥2.45N.m
- Shaft diameter: 6.35mm or 1/4″

### SILVERCNC MK-M26D-20 Tool Setter

- **Type**: CNC tool setter for machining centers (Z-axis zero setting)
- **Configuration**: Normally closed high accuracy design with 6-core cable
- **Features**:
  - IP67 waterproof and dustproof construction
  - Automatic tool setting capability
  - Zero pretravel (immediate signal on contact)
  - Tungsten carbide contact surface with grinding 4s finish
  - Built-in LED indicator (OFF idle / ON operating)
  - Over-travel protection with built-in microswitch
  - 6-core cable (improved noise immunity and reliability) - 4 wires used by our application
  - Normally closed (NC) contact (safer - detects disconnections)
  - Oil-resistant cable with 5m standard length
- **Physical Specifications:**
  - Contact Diameter: Ø20mm
  - Contact Material: Tungsten carbide
  - Surface Finishing: Grinding 4s (high precision)
  - Stroke: 5mm
- **Electrical Specifications:**
  - Contact Type: NC (Normally Closed)
  - Operating Voltage: DC24V ±10%
  - Current Rating: 20mA maximum (resistive load)
  - Recommended Steady Current: 10mA or less
  - Cable: 6-core, φ4.8mm diameter, oil-resistant, 5m standard length - 4 wires used by our application
  - LED Indicator: Built-in status indicator
  - Over-travel Protection: NC output mode for emergency stop
- **Performance Specifications:**
  - Repeatability: 0.002mm (at recommended operating speed)
  - Contact Force: 1.5N (vertical installation position)
  - Contact Life: 3 million cycles
  - Protection Rating: IP67
  - Operating Temperature: -25°C to 70°C
  - Recommended Operating Speed: 50-200mm/min
  - Maximum Tool Diameter: <20mm (must be smaller than contact diameter)

### FORYON X/Y/Z Touch Probe

- **Type**: 3-axis (X/Y/Z) touch probe for CNC machining
- **Configuration**: Precise Head and Play design with multi-axis sensing
- **Features**:
  - X, Y, and Z axis probing capability
  - Plug-and-play design
  - Multi-color options available (G/R/B/L - Green/Red/Blue/possibly other colors)
  - Precise touch detection
  - Compatible with multiple CNC platforms
- **Specifications**:
  - Axes Detected: X, Y, Z (3-axis probing)
  - Contact Type: Normally open
  - Signal Output: Digital (switch closure on contact)
  - Probe Tip: Precision ground (typically tungsten carbide or hardened steel)
  - Repeatability: High precision (specific tolerance not specified by manufacturer)

### Duet3D 6HC controller

The Duet3D 6HC controller serves as the brain of this CNC machine, running RepRap firmware optimized for precise motion control and machining operations. This controller is specifically well-suited for CNC applications due to several key characteristics:

- **Multi-axis Control**: Supports up to 8 axes of movement with independent control of X, Y, Z axes plus additional rotational axes for complex machining operations
- **High-speed Motion**: Capable of handling high-frequency step signals required for precise CNC cutting operations with minimal latency
- **Advanced Motor Drivers**: Integrated motor drivers that provide precise current control and can handle the higher currents typically required by CNC stepper motors
- **Precision Timing**: Built-in high-resolution timers ensure accurate timing for spindle speed control and precise coordinate movement
- **Multiple I/O Options**: Extensive digital and analog input/output capabilities for connecting various CNC peripherals including spindle controllers, coolant pumps, and safety sensors
- **G-code Processing**: Robust G-code interpretation engine that supports complex machining operations and toolpath optimization
- **Network Connectivity**: Built-in Ethernet and WiFi capabilities enable remote monitoring and control of CNC operations
- **Heating Control**: Integrated temperature control for spindle and workpiece heating when required for specific materials
- **Safety Features**: Comprehensive safety monitoring including emergency stop inputs and position monitoring to prevent collisions
- **Expandability**: Support for additional expansion boards and modules to extend functionality as needed

The controller's versatility allows it to be configured specifically for CNC operations while maintaining the flexibility to support other machining tasks, making it an ideal choice for this hobby CNC build.

### Opt Lasers XF+ 6W Plug & Play Laser Kit

The Opt Lasers XF+ 6W Plug & Play Laser Kit represents a significant upgrade that transforms this CNC machine from a purely router-based system into a versatile hybrid machine capable of both CNC routing and laser operations. This kit enables the machine to perform laser cutting, engraving, and marking tasks with precision and efficiency.

Key features of the Opt Lasers XF+ 6W kit include:

- **Power Output**: 6 Watt laser output providing sufficient power for most materials including wood, acrylic, fabric, and thin metals
- **Plug & Play Design**: Simple installation process that doesn't require extensive modifications to the existing CNC setup
- **Compatibility**: Designed specifically for use with Duet3D controllers and compatible with the Ultimate Bee's mechanical specifications
- **Precision Control**: Allows for precise laser positioning and control through the same G-code commands used for CNC operations
- **Material Versatility**: Capable of processing a wide range of materials commonly used in hobbyist and small-scale manufacturing projects

This upgrade transforms the machine from a single-purpose CNC router into a multi-functional tool that can handle both cutting and engraving tasks. The laser kit integrates seamlessly with the existing Duet3D 6HC controller, allowing operators to switch between router and laser modes without requiring additional hardware or complex configuration changes.

The ability to use the same machine for both CNC routing and laser operations significantly increases its utility and value, making it an ideal choice for hobbyists and small workshops looking to expand their capabilities without investing in separate equipment.

### Vevor Electronics Enclosure

This enclosure will hold the Duet3D controller, Meanwell PSU, and associated components. Connectors will be installed to connect peripherals such as limit switches, stepper motors, VFD, and e-stop which are located outside the box. Components mounted directly to the enclosure will also include wifi antenna, laser adapter for Opt Lasers XF+, E-Stop, Cycle Start, Pause/Feed Hold, and Reset button. When a clear industry standard (official or de facto) does not drive otherwise, connectors on the outside of the enclosure will be biased towards GX style (aviation) connectors to benefit from the strong mechanical connection

- NEMA 4X Steel Electrical Box
- 20" x 20" x 6" outer dimensions
- Galvanized back plate w/ 5 16" aluminum DIN rails mounted

## Duet3D 6HC Peripheral Connections

This section describes the connection between the Duet3D 6HC main board and various peripherals. While things like wire color may be specified to help create an intuitive setup, it is important to note than in many cases the connections described as a direct connection to peripherals in many cases the actual implementation will include intermediate connection points such as connectors and terminal blocks. In general, any connection between devices that are attached to the back plate of the enclosure will be direct while any connection between a component on the back plane and a component that is not on the back plane will at minimum go through a terminal block which is mounted to a DIN rail on the back plane.

| Duet3D 6HC Connection Header   | Function               | Details                                                                       |
|--------------------------------|------------------------|-------------------------------------------------------------------------------|
| IO_0                           | Reserved               | IO_0 shares resources with PanelDue and won't be used directly in this build  |
| IO_1                           | Reserved               | IO_1 shares resources with RS485 (modbus) which is needed for spindle control |
| IO_2                           | E-Stop                 | Red to "in" pin, black to GND                                                 |
| IO_3                           | Tool Setter Probe      | Brown to "in", Orange to GND                                                  |
| IO_4                           | Tool Setter Safety     | Green to "in", Blue to GND                                                    |
| IO_5                           | X-Axis Limits          | Min/Max wired in series. Brown to VCC, Blue to GND, Black to "in" pin         |
| IO_6                           | Y-Axis Limits          | see above                                                                     |
| IO_7                           | Z-Axis Limits          | see above                                                                     |
| IO_8                           | XYZ Touch Probe        | Red to "in", Black to GND                                                     |
| IO_9 (PWM)                     | Laser Adapter          | GND to Adapter "D" (GND) terminal, "out" to "B" (TTL), +5V to "C" (enable)    |
| TEMP_0                         | Cycle Start Button     |                                                                               |
| TEMP_1                         | Pause/Feed Hold Button |                                                                               |
| RESET                          | Reset Button           | Hard reset of controller                                                      |
| OUT_1                          | TBD                    | Likely contactor or relay addition                                            |
| OUT_2                          | TBD                    | Likely contactor or relay addition                                            |
| OUT_3                          | TBD                    | Likely contactor or relay addition                                            |
| OUT_4                          | Fan                    | Constant intake to case for cooling and positive pressure                     |
| OUT_5                          | Fan                    | Temperature driven to pull heat from drivers                                  |
| OUT_6                          | Fan                    | Temperature driven to exhaust warm air from case                              |
| DRIVER_0                       | X Axis Stepper         | Green to A1, Black to A2, Red to B1, Blue to B2                               |
| DRIVER_1                       | Y1 Axis Stepper        | Green to A1, Black to A2, Red to B1, Blue to B2                               |
| DRIVER_2                       | Y2 Axis Stepper        | Green to A1, Black to A2, Red to B1, Blue to B2                               |
| DRIVER_3                       | Z Axis Stepper         | Green to A1, Black to A2, Red to B1, Blue to B2                               |
| ESP                            | Duet Wifi              | Wireless network connection (antenna outside enclosure)                       |
| PANEL_DUE                      | Pendant                | Planned custom pendant to be added in near future                             |
| POWER IN                       | Meanwell LRS-350-24    | 24V Volt Power Supply                                                         |
| RS485                          | VFD RS485              | Red to A, Black to B                                                          |
| DS_LED                         | NeoPixel Strip         | 3.3ft, 144 LED                                                                |

> NOTE: Laser Adapter IO_9 "enable" will be high from the board, so the adapter's key safety interlock is important

