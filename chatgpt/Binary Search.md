Model: GPT-4

> 1 / 1
> 
> Write a self-contained function block in 61131-3 structured text that implements a binary search to find an integer in an array of 100 integers.

2 / 2

Here's a self-contained function block implementing a binary search algorithm in IEC 61131-3 Structured Text language. This function block will search for an integer in an array of 100 integers:

iecst

```iecst
FUNCTION_BLOCK FB_BinarySearch
VAR_INPUT
    ArrayToSearch: ARRAY[1..100] OF INT;
    TargetValue: INT;
END_VAR
VAR_OUTPUT
    ResultIndex: INT; // The index of the target value if found, or -1 if not found
END_VAR
VAR
    Left: INT := 1;
    Right: INT := 100;
    Middle: INT;
END_VAR
METHOD Search: INT
    Left := 1;
    Right := 100;
    WHILE Left <= Right DO
        Middle := (Left + Right) DIV 2;
        IF ArrayToSearch[Middle] = TargetValue THEN
            RETURN Middle;
        ELSIF ArrayToSearch[Middle] < TargetValue THEN
            Left := Middle + 1;
        ELSE
            Right := Middle - 1;
        END_IF;
    END_WHILE;
    RETURN -1;
END_METHOD
END_FUNCTION_BLOCK
```

This function block `FB_BinarySearch` has two inputs: `ArrayToSearch` for the array of integers to be searched and `TargetValue` for the integer value you want to find. The output `ResultIndex` will contain the index of the target value in the array if found, or -1 if not found. To perform the search, call the `Search` method which returns the index of the target value or -1 if not found.