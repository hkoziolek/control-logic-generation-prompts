# Batch Control Recipe & Program

**Human:**
Give an isa-88 batch control recpie of an adhesive production. Formulate step 3 as IEC 61131-3 ST program.

***

**Assistant:**

ISA-88 Batch Control Recipe for Adhesive Production:

1. Add water to mixing tank
2. Add dispersant to mixing tank
3. Add adhesive raw materials to mixing tank
4. Mix ingredients for 10 minutes
5. Add catalyst to mixing tank
6. Mix for 5 minutes
7. Transfer adhesive to holding tank
8. Quality control check
9. If approved, transfer adhesive to packaging


IEC 61131-3 ST program for Step 3:

```
PROGRAM MIX_INGREDIENTS
VAR
    MixingTank : BOOL;
    AdhesiveRawMaterials : ARRAY[1..5] OF REAL; (*assuming there are 5 raw materials*)
    Dispersant : REAL;
    MixTime : INT;
END_VAR
(*Set initial values*)
MixingTank := TRUE;
AdhesiveRawMaterials[1] := 100.0; (*Raw Material 1*)
AdhesiveRawMaterials[2] := 50.0; (*Raw Material 2*)
AdhesiveRawMaterials[3] := 75.0; (*Raw Material 3*)
AdhesiveRawMaterials[4] := 40.0; (*Raw Material 4*)
AdhesiveRawMaterials[5] := 20.0; (*Raw Material 5*)
Dispersant := 5.0; (*Amount of dispersant*)
MixTime := 10; (*Mixing time in minutes*)

(*Start mixing*)
WHILE MixTime > 0 DO
    (*Mix each raw material*)
    FOR i := 1 TO 5 DO
        IF AdhesiveRawMaterials[i] > 0 THEN
            (*Add raw material to mixing tank*)
            MixingTank := TRUE;
            (*Decrease amount of raw material*)
            AdhesiveRawMaterials[i] := AdhesiveRawMaterials[i] - 1;
        END_IF
    END_FOR
    (*Add dispersant to mixing tank*)
    MixingTank := TRUE;
    (*Decrease dispersant amount*)
    Dispersant := Dispersant - 0.1;
    (*Decrease mixing time*)
    MixTime := MixTime - 1;
END_WHILE

(*Stop mixing*)
MixingTank := FALSE;

```

Note: This program is just an example and would need to be adapted to the specific requirements of the adhesive production process.


***

Exported on March 11, 2023 10:10 PM.