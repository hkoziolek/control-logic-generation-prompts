Model: Default (GPT-3.5)

> Write a PLC program in ST according to IEC 61131-3, to create an Entry/Exit Control of the Underground Car Park. These are sensors in the system: X1: Photoelectric switch at the ground floor entry/exit. X1 will be ON when a car passes. X2: Photoelectric switch at the basement entry/exit. X2 will be ON when a car passes. M1: M1 will be ON for one scan cycle when a car from the ground floor passes X1. M2: M2 will be ON for one scan cycle when a car from the basement passes X1. M3: M3 will be ON for one scan cycle when a car from the basement passes X2. M4: M4 will be ON for one scan cycle when a car from the ground floor passes X2. Intermidiate variables: M20: M20 = ON during the process of a car entering the passage from the ground floor. M30: M30 = ON during the process of a car entering the passage from the basement. These are outputs devices in the system: Y1: Red lights at the entry/exit of the ground floor and the basement. Y2: Green lights at the entry/exit of the ground floor and the basement. Description of the process: The entry/exit of the underground car park is a single lane passage which needs the traffic lights to control the cars. Red lights prohibit cars entering or leaving while green lights allowcars to enter or leave. When a car enters the passage from the entry of the ground floor, the red lights both on the ground floor and the basement will be ON, and the green lights will be OFF. Any car entering or leaving is prohibited during the process till the car passes through the passage completely. When the passage is clear, the green lights will be ON again and allow other cars entering from the ground floor or the basement.Similarly, when a car leaves the basement and enters the passage, any other car entering or leaving is prohibited till the car passes from the passage to the ground completely.When PLC runs, the initial setting of traffic lights will be green lights ON and red lights OFF.

Here is a PLC program in ST according to IEC 61131-3 to create an entry/exit control of the underground car park:

go

```go
PROGRAM Entry_Exit_Control
VAR
    X1, X2 : BOOL;   // Input sensors
    M1, M2, M3, M4, M20, M30 : BOOL;   // Intermediate variables
    Y1, Y2 : BOOL;   // Output devices
END_VAR

// Initialization
Y1 := FALSE;   // Red lights at the entry/exit of the ground floor and the basement
Y2 := TRUE;    // Green lights at the entry/exit of the ground floor and the basement

// Main program
IF M20 OR M30 THEN   // Car is in the passage
    Y1 := TRUE;      // Red lights ON
    Y2 := FALSE;     // Green lights OFF
ELSE                // Car is not in the passage
    Y1 := FALSE;     // Red lights OFF
    Y2 := TRUE;      // Green lights ON
END_IF

// Process of a car entering from the ground floor
IF X1 AND NOT M20 THEN   // Car is entering from the ground floor
    M20 := TRUE;         // Car in the passage
    Y1 := TRUE;          // Red lights ON
    Y2 := FALSE;         // Green lights OFF
    M1 := TRUE;          // Car sensor ON for one scan cycle
END_IF

IF M1 THEN              // Car sensor ON for one scan cycle
    M20 := FALSE;        // Car left the passage
END_IF

// Process of a car entering from the basement
IF X2 AND NOT M30 THEN  // Car is entering from the basement
    M30 := TRUE;        // Car in the passage
    Y1 := TRUE;         // Red lights ON
    Y2 := FALSE;        // Green lights OFF
    M3 := TRUE;         // Car sensor ON for one scan cycle
END_IF

IF M3 THEN              // Car sensor ON for one scan cycle
    M30 := FALSE;       // Car left the passage
END_IF

// Process of a car leaving from the basement
IF X1 AND NOT M20 THEN   // Car is leaving from the basement
    M20 := TRUE;         // Car in the passage
    Y1 := TRUE;          // Red lights ON
    Y2 := FALSE;         // Green lights OFF
    M4 := TRUE;          // Car sensor ON for one scan cycle
END_IF

IF M4 THEN              // Car sensor ON for one scan cycle
    M20 := FALSE;        // Car left the passage
END_IF

// Process of a car leaving from the ground floor
IF X2 AND NOT M30 THEN  // Car is leaving from the ground floor
    M30 := TRUE;        // Car in the passage
    Y1 := TRUE;         // Red lights ON
    Y2 := FALSE;        // Green lights OFF
    M2 := TRUE;         // Car sensor ON for one scan cycle
END_IF

IF M2 THEN              // Car sensor ON for one scan cycle
    M30 := FALSE;       // Car left the passage
END_IF
```

In this program, `X1` and `X2` are input sensors that detect when a car passes through the photoelectric switches at the ground floor and basement entry/exit points respectively. `M1`, `M2`, `M3`, `M4`, `M20`, and `M30` are intermediate variables that keep track of the state of the system. `Y1` and `Y2`

> continue

are output devices that control the traffic lights at the entry/exit points.

The program starts with the initialization of the output variables `Y1` and `Y2`. The red lights at the entry/exit points are initially OFF, and the green lights are ON.

The main program then checks if there is a car in the passage or not. If there is a car in the passage, the red lights will be ON, and the green lights will be OFF. Otherwise, the red lights will be OFF, and the green lights will be ON.

The program then checks the status of the input sensors `X1` and `X2` to determine if a car is entering or leaving the passage. If a car is entering the passage from the ground floor, the program sets the `M20` variable to `TRUE` to indicate that the car is in the passage. The program also turns ON the red lights and turns OFF the green lights to indicate that other cars should not enter or leave the passage until the current car has passed through the passage completely. The program then sets the `M1` variable to `TRUE` to keep track of the car sensor status for one scan cycle.

Once the car has passed through the passage, the program resets the `M20` variable to `FALSE` to indicate that the passage is now clear.

Similar steps are taken for a car entering from the basement (`X2`), a car leaving from the basement (`X1`), and a car leaving from the ground floor (`X2`). The program sets the `M30`, `M4`, and `M2` variables respectively to indicate that a car is in the passage, and resets them once the car has passed through.

Overall, this program implements the entry/exit control of the underground car park by controlling the traffic lights and prohibiting other cars from entering or leaving the passage while a car is passing through.