Model: GPT-4

> 1 / 1
> 
> Write a self-contained function block in 61131-3 structured text that compares two real inputs up to n digits.

1 / 1

Here's a self-contained function block in IEC 61131-3 Structured Text that compares two real inputs (Real1 and Real2) up to n digits (Precision):

iecst

```iecst
FUNCTION_BLOCK RealCompare
VAR_INPUT
  Real1 : REAL;
  Real2 : REAL;
  Precision : UDINT;
END_VAR

VAR_OUTPUT
  Result : INT; // -1 if Real1 < Real2, 0 if Real1 = Real2, 1 if Real1 > Real2
END_VAR

METHOD Compare : INT;
VAR
  RoundedReal1 : REAL;
  RoundedReal2 : REAL;
  Factor : REAL;
END_VAR

  Factor := REAL(10 ** Precision);
  RoundedReal1 := ROUND(Real1 * Factor);
  RoundedReal2 := ROUND(Real2 * Factor);

  IF RoundedReal1 < RoundedReal2 THEN
    Compare := -1;
  ELSIF RoundedReal1 > RoundedReal2 THEN
    Compare := 1;
  ELSE
    Compare := 0;
  END_IF;
END_METHOD
END_FUNCTION_BLOCK
```

To use this function block, you will need to create an instance of it, set the input values (Real1, Real2, and Precision), and then call the Compare method. The Result variable will hold the comparison result (-1, 0, or 1).