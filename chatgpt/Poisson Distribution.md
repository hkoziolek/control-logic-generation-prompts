Model: GPT-4

> 1 / 1
> 
> Write a self-contained function block in 61131-3 to compute a Poisson distribution.

1 / 1

In IEC 61131-3, the Function Block (FB) can be written using Structured Text (ST) language. Here is a self-contained function block for computing the Poisson distribution:

iecst

```iecst
FUNCTION_BLOCK FB_Poisson
VAR_INPUT
    lambda: REAL; // Poisson distribution's rate parameter (average events per interval)
    k: INT; // Number of events (non-negative integer)
END_VAR

VAR_OUTPUT
    P: REAL; // Probability of k events occurring in the given interval
END_VAR

VAR
    i: INT;
    sum: REAL;
    e_lambda: REAL; // e^(-lambda)
    lambda_pow_k: REAL; // lambda^k
    fact_k: REAL; // k!
END_VAR

METHOD Calculate: BOOL
    e_lambda := EXP(-lambda);
    lambda_pow_k := 1.0;
    fact_k := 1.0;
    sum := 0.0;

    FOR i := 0 TO k DO
        IF i > 0 THEN
            lambda_pow_k := lambda_pow_k * lambda;
            fact_k := fact_k * i;
        END_IF;
        sum := sum + (lambda_pow_k / fact_k);
    END_FOR;

    P := e_lambda * sum;
    RETURN TRUE; // Calculation completed successfully
END_METHOD
END_FUNCTION_BLOCK
```

This function block can be used to compute the Poisson distribution for a given rate parameter `lambda` and number of events `k`. The probability is returned as output `P`. The `Calculate` method should be called to perform the computation.

Usage example:

iecst

```iecst
PROGRAM Main
VAR
    myPoisson: FB_Poisson;
    result: BOOL;
END_VAR

myPoisson.lambda := 5.0;
myPoisson.k := 3;

result := myPoisson.Calculate();

IF result THEN
    // Use myPoisson.P as the computed probability
END_IF
END_PROGRAM
```