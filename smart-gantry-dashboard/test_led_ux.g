; test_led_ux.g - Full Triple-Zone UX Verification
; Zones: [Status 20] [Task 104] [Progress 20]

var testProgress = 0.0

while var.testProgress <= 100.0
    ; 1. Calculate Progress Variables (Right Zone)
    var scale = var.testProgress * 0.20
    var fullLeds = floor(var.scale)
    var partialIntensity = floor((var.scale - var.fullLeds) * 200)

    ; 2. Determine Simulated Status Color (Left Zone)
    ; This cycles through our UX logic as the "job" progresses
    var r = 0 | var u = 0 | var b = 0
    if var.testProgress < 25
        set var.u = 200                 ; Green (Running)
    elif var.testProgress < 50
        set var.r = 255 | set var.u = 180 ; Yellow (Paused/Attention)
    elif var.testProgress < 75
        set var.r = 255 | set var.b = 255 ; Magenta (Tool Change)
    else
        ; Simulated Flashing Red (Emergency)
        if (floor(var.testProgress) % 2 == 0)
            set var.r = 255
        else
            set var.r = 0

    ; 3. Update the Strip (The Chain)
    
    ; ZONE A: Status Tower (Left 20)
    M150 E0 R{var.r} U{var.u} B{var.b} S20 F1
    
    ; ZONE B: Task Lighting (Center 104)
    M150 E0 R200 U200 B200 S104 F1
    
    ; ZONE C: Progress Bar (Right 20)
    if var.fullLeds > 0
        M150 E0 R0 U0 B200 S{var.fullLeds} F1
    
    if var.fullLeds < 20
        M150 E0 R0 U0 B{var.partialIntensity} S1 F1
    
    var remaining = 19 - var.fullLeds
    if var.remaining > 0
        M150 E0 R0 U0 B5 S{var.remaining} F0
    else
        M150 E0 R0 U0 B0 S0 F0 ; Terminate chain

    ; 4. Increment and Dwell
    set var.testProgress = var.testProgress + 1.0
    G4 P50 ; Fast 50ms steps for a quick 5-second show
    
; Final Success Signal: Whole gantry Green
M150 E0 R0 U255 B0 S144 F0
G4 S1
M150 E0 R40 U30 B5 S144 F0 ; Return to Warm Standby
