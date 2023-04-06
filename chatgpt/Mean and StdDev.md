Model: GPT-4

> Write a self-contained function block in IEC 61131-3 Structured Text to compute the mean and standard deviation for a input array of 100 integers.

Here is a self-contained function block in IEC 61131-3 Structured Text that computes the mean and standard deviation for an input array of 100 integers:

css

```css
FUNCTION_BLOCK MeanAndStandardDeviation
VAR_INPUT
    InputArray: ARRAY [1..100] OF INT;
END_VAR

VAR_OUTPUT
    Mean: REAL;
    StandardDeviation: REAL;
END_VAR

VAR
    Sum: REAL := 0;
    SumOfSquares: REAL := 0;
    ArrayLength: INT := 100;
    i: INT;
END_VAR

METHOD Compute
    Sum := 0;
    SumOfSquares := 0;
    FOR i := 1 TO ArrayLength DO
        Sum := Sum + InputArray[i];
        SumOfSquares := SumOfSquares + (InputArray[i] * InputArray[i]);
    END_FOR

    Mean := Sum / REAL(ArrayLength);
    
    StandardDeviation := SQRT((SumOfSquares / REAL(ArrayLength)) - (Mean * Mean));
END_METHOD
END_FUNCTION_BLOCK
```

To use this function block, create an instance of it, and call the "Compute" method. The "Mean" and "StandardDeviation" variables will be updated with the calculated values.