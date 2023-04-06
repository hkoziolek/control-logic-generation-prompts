Model: GPT-4

> Write a self-contained function block in IEC 61131-3 Structured Text to compute a linear interpolation.

Here's a self-contained function block in IEC 61131-3 Structured Text for computing linear interpolation:

iecst

```iecst
FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    x1, y1 : REAL;
    x2, y2 : REAL;
    x : REAL;
END_VAR

VAR_OUTPUT
    y : REAL;
END_VAR

METHOD Compute: REAL
    VAR
        deltaX, deltaY, slope, intercept : REAL;
    END_VAR
BEGIN
    IF x1 = x2 THEN
        RETURN y1;
    END_IF;

    deltaX := x2 - x1;
    deltaY := y2 - y1;
    slope := deltaY / deltaX;
    intercept := y1 - (slope * x1);

    y := (slope * x) + intercept;

    RETURN y;
END_METHOD
END_FUNCTION_BLOCK
```

This function block, named "LinearInterpolation", accepts 5 inputs: x1, y1, x2, y2, and x. It computes the linear interpolation of the point (x, y) on the line defined by the points (x1, y1) and (x2, y2). The result is returned as an output variable named "y".

The Compute method is used to perform the calculation. If x1 and x2 are equal, the function returns y1 as the result. Otherwise, it calculates the slope and intercept of the line, then computes the y-value based on the input x-value.