# Duet3D 6HC Configuration Requirements

This document outlines all the requirements that must be met to configure a Duet3D 6HC controller for the Bulkman3D Ultimate Bee CNC machine with all specified peripherals. The requirements are organized in checklist format for easy validation.

## Table of Contents

1. [General System Configuration](#general-system-configuration)
2. [Motor and Axis Configuration](#motor-and-axis-configuration)
3. [Spindle/VFD Control](#spindlevfd-control)
4. [Tool Setter Configuration](#tool-setter-configuration)
5. [Touch Probe Configuration](#touch-probe-configuration)
6. [Laser Configuration](#laser-configuration)
7. [Safety Systems](#safety-systems)
8. [I/O and Peripheral Connections](#io-and-peripheral-connections)
9. [Network and Communication](#network-and-communication)
10. [Fan and Cooling Control](#fan-and-cooling-control)

## General System Configuration

- [ ] Configure CNC mode using M453 command
- [ ] Set up proper machine coordinate system (G54) 
- [ ] Configure firmware for spindle control using M453
- [ ] Enable CNC mode with proper tool definitions
- [ ] Set up basic G-code parameters (G21, G90)
- [ ] Configure maximum feedrates and accelerations
- [ ] Set up steps per mm for all axes (X, Y, Z)  
- [ ] Configure axis limits and endstops properly
- [ ] Configure microstepping settings for motors
- [ ] Set up proper coordinate system offsets

## Motor and Axis Configuration

### NEMA 23 Stepper Motors

- [ ] Configure motor drivers for NEMA 23 motors (1.8° step angle)
- [ ] Set appropriate current limits for motors (3.0A rated)
- [ ] Configure driver microstepping (typically 1/16 step)
- [ ] Verify proper wiring of motor connections to drivers
- [ ] Configure motor direction and axis mapping

### X-Axis Stepper Motor

- [ ] Configure DRIVER_0 for X-axis stepper motor
- [ ] Set correct wiring: Green to A1, Black to A2, Red to B1, Blue to B2
- [ ] Configure proper current settings for X-axis motor
- [ ] Set steps per mm for X-axis (based on motor and mechanical setup)

### Y-Axis Stepper Motors

- [ ] Configure DRIVER_1 for Y1 axis stepper motor
- [ ] Configure DRIVER_2 for Y2 axis stepper motor
- [ ] Set correct wiring for both Y-axis motors
- [ ] Configure proper current settings for Y-axis motors
- [ ] Set steps per mm for Y-axis (based on motor and mechanical setup)
- [ ] Configure Y-axis gantry configuration if applicable

### Z-Axis Stepper Motor

- [ ] Configure DRIVER_3 for Z-axis stepper motor
- [ ] Set correct wiring: Green to A1, Black to A2, Red to B1, Blue to B2
- [ ] Configure proper current settings for Z-axis motor
- [ ] Set steps per mm for Z-axis (based on motor and mechanical setup)

## Spindle/VFD Control

### Huanyang HY02D211B VFD Configuration

- [ ] Configure RS485 communication with VFD using M950 command
- [ ] Set up proper Modbus RTU parameters (address 1, 9600 baud, 8N1)
- [ ] Configure VFD to use RS485 for both command and frequency source (PD001=2, PD002=2)
- [ ] Set maximum frequency in VFD to 400Hz (for 24K RPM spindle)
- [ ] Set base frequency in VFD to 400Hz 
- [ ] Configure acceleration time (PD007) to 3 seconds
- [ ] Configure deceleration time (PD008) to 3 seconds
- [ ] Set motor rated parameters in VFD (PD143-PD146)
- [ ] Configure VFD for proper power supply (110V single-phase input)
- [ ] Verify proper wiring of RS485 connections between Duet and VFD
- [ ] Configure VFD for proper grounding (PE terminal connected to earth ground)

### Duet3D 6HC Spindle Configuration

- [ ] Create spindle definition using M950 R0 C"rs485" Q1 command
- [ ] Define tool 0 with spindle using M563 P0 R0 command  
- [ ] Configure spindle speed range (M950 R0 L0:24000)
- [ ] Set up proper spindle commands for M3, M4, M5 G-code operations
- [ ] Configure spindle control parameters in CNC mode
- [ ] Verify proper firmware version compatibility (RepRapFirmware 3.6+ recommended)

## Tool Setter Configuration

### SILVERCNC MK-M26D-20 Tool Setter

- [ ] Configure IO_3 as input for tool setter probe (M542 P3 S1)
- [ ] Set tool setter probe to NC (Normally Closed) mode (M543 P3 S0)
- [ ] Configure IO_4 as input for tool setter safety (M542 P4 S1)
- [ ] Set tool setter safety to NC (Normally Closed) mode (M543 P4 S0)
- [ ] Configure tool setter probe test command (G31 P1 Z-10 F1000)
- [ ] Define tool 0 to use the tool setter probe (M561 P0 S1)
- [ ] Verify proper wiring of tool setter connections:
  - IO_3 Brown wire to "in" pin, Orange wire to GND
  - IO_4 Green wire to "in" pin, Blue wire to GND
- [ ] Test tool setter functionality in firmware
- [ ] Set up tool setter calibration routine

## Touch Probe Configuration

### FORYON X/Y/Z Touch Probe

- [ ] Configure IO_8 as input for XYZ touch probe (M542 P8 S1)
- [ ] Set proper wiring: Red to "in", Black to GND
- [ ] Configure probe contact type as Normally Open (NO)  
- [ ] Set up probe parameters and calibration
- [ ] Configure probe operation in firmware
- [ ] Test touch probe functionality

## Laser Configuration

### Opt Lasers XF+ 6W Laser Kit

- [ ] Configure laser mode using M452 command with appropriate pin assignment
- [ ] Set up proper PWM output for laser control (OUT9 recommended)
- [ ] Configure laser power range from 0 to 255 (8-bit scale)
- [ ] Set appropriate PWM frequency (1kHz typical, adjustable)
- [ ] Define tool 0 as laser (M563 P0 S"Laser")
- [ ] Configure tool offsets for laser position
- [ ] Set up proper laser safety interlocks:
  - E-Stop wired to adapter E-STOP terminals  
  - Key switch wired to adapter KEY_SW terminals
- [ ] Configure laser head power supply connections
- [ ] Test laser operation and safety features
- [ ] Set up laser calibration procedures

## Safety Systems

### Emergency Stop (E-Stop)

- [ ] Configure IO_2 for E-Stop functionality (Red to "in" pin, black to GND)
- [ ] Implement proper emergency stop logic in firmware
- [ ] Verify E-stop functionality works with all safety systems
- [ ] Test E-stop operation in various system states

### Safety Interlocks

- [ ] Configure all safety switches properly for CNC operation
- [ ] Implement automatic safety disarming when safety conditions are violated
- [ ] Set up proper interlock circuits for laser safety
- [ ] Verify emergency stop works with spindle, laser, and other systems

## I/O and Peripheral Connections

### Input/Output Configuration

- [ ] Leave IO_0 unconfigured, but include a placeholder comment acknowledging it as reserved (shares resources with PanelDue)
- [ ] Leave IO_1 as unconfigured, but reserved (shares resources with RS485 for spindle control)
- [ ] Configure IO_2 for E-Stop input
- [ ] Configure IO_3 for tool setter probe input
- [ ] Configure IO_4 for tool setter safety input
- [ ] Configure IO_5 for X-axis limits (Min/Max wired in series)
- [ ] Configure IO_6 for Y-axis limits (Min/Max wired in series)
- [ ] Configure IO_7 for Z-axis limits (Min/Max wired in series)
- [ ] Configure IO_8 for XYZ touch probe input
- [ ] Configure IO_9 (PWM) for laser adapter
- [ ] Configure TEMP_0 for Cycle Start button
- [ ] Configure TEMP_1 for Pause/Feed Hold button
- [ ] Configure RESET for Reset Button

### Motor Driver Connections

- [ ] Verify DRIVER_0 connection to X-axis stepper motor
- [ ] Verify DRIVER_1 connection to Y1 axis stepper motor  
- [ ] Verify DRIVER_2 connection to Y2 axis stepper motor
- [ ] Verify DRIVER_3 connection to Z-axis stepper motor

## Network and Communication

### WiFi Configuration

- [ ] Configure network settings using M552, M553, M554 commands
- [ ] Set up proper hostname (M553 S"reprap")
- [ ] Configure network connectivity for remote monitoring
- [ ] Enable WiFi with appropriate security settings
- [ ] Verify network communication works properly

### Ethernet Configuration

- [ ] Configure static IP address for Ethernet connection (M556)
- [ ] Set up proper subnet mask (M557)
- [ ] Enable Ethernet connectivity
- [ ] Verify proper network configuration for CNC operations

## Fan and Cooling Control

### Fan Configuration

- [ ] Configure OUT_4 as constant intake fan for cooling and positive pressure
- [ ] Configure OUT_5 as temperature-driven fan to pull heat from drivers
- [ ] Configure OUT_6 as temperature-driven fan to exhaust warm air from case
- [ ] Set up appropriate fan control parameters based on thermal monitoring
- [ ] Verify proper airflow configuration for system cooling

## Additional Requirements

### System Documentation and Testing

- [ ] Document all configuration parameters in config.g file
- [ ] Create comprehensive test routines for each component
- [ ] Implement proper backup procedures for firmware configurations
- [ ] Set up logging and monitoring capabilities
- [ ] Create user manuals for operation and safety
- [ ] Establish maintenance schedules for all system components
