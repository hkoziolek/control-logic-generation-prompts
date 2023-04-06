Model: GPT-4

> 1 / 1
> 
> Write a self-contained function block in 61131-3 structured text that converts fahrenheit to celsius.

1 / 1

In IEC 61131-3 Structured Text (ST) language, here's a self-contained function block that converts Fahrenheit to Celsius:

iecst

```iecst
FUNCTION_BLOCK FB_FahrenheitToCelsius
    VAR_INPUT
        FahrenheitTemp: REAL;
    END_VAR

    VAR_OUTPUT
        CelsiusTemp: REAL;
    END_VAR

    METHOD Convert: REAL;
END_FUNCTION_BLOCK

METHOD FB_FahrenheitToCelsius.Convert
    CelsiusTemp := (FahrenheitTemp - 32) * 5 / 9;
    RETURN CelsiusTemp;
END_METHOD
```

This function block, named `FB_FahrenheitToCelsius`, takes an input `FahrenheitTemp` of type REAL and has an output variable `CelsiusTemp` of type REAL. The method `Convert` is responsible for the conversion from Fahrenheit to Celsius, and it returns the calculated Celsius value.

To use this function block, you need to create an instance of it and call the `Convert` method. Here's an example of how to use this function block in a main program:

iecst

```iecst
PROGRAM Main
    VAR
        TemperatureConverter: FB_FahrenheitToCelsius;
        InputFahrenheit: REAL := 100.0;
        OutputCelsius: REAL;
    END_VAR
END_PROGRAM

OutputCelsius := TemperatureConverter(Convert := InputFahrenheit);
```

This main program initializes a `TemperatureConverter` instance of the `FB_FahrenheitToCelsius` function block and assigns the value 100.0 to the `InputFahrenheit` variable. The conversion method is then called, and the result is stored in the `OutputCelsius` variable.