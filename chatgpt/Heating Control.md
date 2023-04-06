Model: Default (GPT-3.5)

> Write a self-contained 61131-3 structured text program, not a function block, to control the temperature of a heating system. The system should automatically turn on and off based on three temperature sensors and maintain a constant temperature range between 20 and 22 degree celsius.

Here's an example program in structured text to control the temperature of a heating system based on three temperature sensors:

css

```css
PROGRAM Heating_Control
VAR
    temperature1 : REAL;
    temperature2 : REAL;
    temperature3 : REAL;
    target_temperature : REAL := 21.0; (* Target temperature range is 20-22°C *)
    heating_on : BOOL := FALSE;
END_VAR

(* Read temperature sensors *)
temperature1 := ReadTemperatureSensor1();
temperature2 := ReadTemperatureSensor2();
temperature3 := ReadTemperatureSensor3();

(* Determine average temperature *)
VAR
    temperature_sum : REAL := temperature1 + temperature2 + temperature3;
    average_temperature : REAL := temperature_sum / 3.0;
END_VAR

(* Check if heating needs to be turned on or off *)
IF (average_temperature < (target_temperature - 0.5)) THEN
    heating_on := TRUE;
ELSIF (average_temperature > (target_temperature + 0.5)) THEN
    heating_on := FALSE;
END_IF

(* Turn heating on or off *)
IF (heating_on) THEN
    TurnOnHeating();
ELSE
    TurnOffHeating();
END_IF

END_PROGRAM
```

This program reads three temperature sensors and calculates the average temperature. If the average temperature falls below the lower limit of the target temperature range (20°C), the heating system is turned on. If the average temperature rises above the upper limit of the target temperature range (22°C), the heating system is turned off. Otherwise, the heating system remains in its current state. The `ReadTemperatureSensorX()` and `TurnOnHeating()`/`TurnOffHeating()` functions would need to be implemented separately depending on the hardware being used.