# Polymerizing Polyvinylchloride: Control Recipe.

**Human:**
give an isa 88 control recipe of batch production of polyvinylchloride by polymerization of vinylchloride monomers

***

**Assistant:**

Sure! Here's an example ISA-88 control recipe for the batch production of polyvinylchloride by polymerization of vinylchloride monomers:

1. Pre-batch Operations:


- Ensure that all equipment is clean and free from any contaminants.
- Check that all necessary raw materials are available in the correct quantities.
- Ensure that all equipment and instruments are calibrated and functioning properly.
- Set up the control system to start the batch process.

<ol start="2">Charging Operations:</li></ol>
- Transfer the correct amount of vinylchloride monomer into the reactor vessel.
- Begin agitating the contents of the reactor to ensure thorough mixing.
- Begin heating the contents of the reactor to the desired temperature.
- Add any necessary initiators or other additives to the reactor.

<ol start="3">Reaction Operations:</li></ol>
- Monitor the temperature, pressure, and agitation of the reactor vessel.
- Allow the polymerization reaction to proceed until the desired conversion has been reached.
- Sample the reaction mixture at regular intervals to ensure that the reaction is proceeding as planned.

<ol start="4">Purification Operations:</li></ol>
- Cool the contents of the reactor vessel to the desired temperature.
- Transfer the contents of the reactor to a purification vessel.
- Add any necessary coagulants or flocculants to the mixture to aid in purification.
- Allow the mixture to settle, and remove any solids that have formed.

<ol start="5">Finishing Operations:</li></ol>
- Filter the purified polymer to remove any remaining solids.
- Dry the polymer to the desired moisture content.
- Package the polymer for shipment.


Throughout the entire process, the control system should monitor all critical process parameters, such as temperature, pressure, and agitation speed, to ensure that the batch is produced according to the desired specifications. Any deviations from the specified process parameters should trigger appropriate alarms or corrective actions to prevent product quality issues.


***

**Human:**
formulate reaction operations as iec 61131-3 st program with typical values and condition for finialization

***

**Assistant:**

Sure! Here's an example IEC 61131-3 ST program for the reaction operations in the production of polyvinylchloride by polymerization of vinylchloride monomers:

```
PROGRAM Polymerization_Reaction
VAR
    Reactor_Temperature : REAL;
    Reactor_Pressure : REAL;
    Reactor_Agitator_Speed : REAL;
    Conversion : REAL;
END_VAR

// Set initial values for process parameters
Reactor_Temperature := 50.0; // °C
Reactor_Pressure := 1.0; // bar
Reactor_Agitator_Speed := 100.0; // rpm
Conversion := 0.0;

// Main program loop
WHILE (Conversion < 99.0) DO
    // Monitor temperature, pressure, and agitation speed
    IF (Reactor_Temperature < 60.0) THEN
        // Increase temperature if too low
        Reactor_Temperature := Reactor_Temperature + 1.0;
    ELSEIF (Reactor_Temperature > 70.0) THEN
        // Decrease temperature if too high
        Reactor_Temperature := Reactor_Temperature - 1.0;
    END_IF
    
    IF (Reactor_Pressure < 2.0) THEN
        // Increase pressure if too low
        Reactor_Pressure := Reactor_Pressure + 0.1;
    ELSEIF (Reactor_Pressure > 3.0) THEN
        // Decrease pressure if too high
        Reactor_Pressure := Reactor_Pressure - 0.1;
    END_IF
    
    IF (Reactor_Agitator_Speed < 200.0) THEN
        // Increase agitation speed if too low
        Reactor_Agitator_Speed := Reactor_Agitator_Speed + 10.0;
    ELSEIF (Reactor_Agitator_Speed > 300.0) THEN
        // Decrease agitation speed if too high
        Reactor_Agitator_Speed := Reactor_Agitator_Speed - 10.0;
    END_IF
    
    // Monitor conversion rate and adjust process as necessary
    Conversion := Get_Conversion_Rate();
    IF (Conversion > 90.0) THEN
        // Slow down the reaction to avoid over-polymerization
        Reactor_Agitator_Speed := Reactor_Agitator_Speed - 10.0;
    ELSEIF (Conversion < 70.0) THEN
        // Speed up the reaction to increase conversion rate
        Reactor_Agitator_Speed := Reactor_Agitator_Speed + 10.0;
    END_IF
    
    // Pause program for 1 second before checking process parameters again
    DELAY 1000;
END_WHILE

// Finalize the reaction
Reactor_Agitator_Speed := 0.0;
Reactor_Temperature := 80.0;
DELAY 5000; // Hold at this temperature for 5 minutes

```

This program uses a simple proportional control scheme to adjust the reactor temperature, pressure, and agitator speed based on their current values. It also monitors the conversion rate and adjusts the agitator speed accordingly to ensure that the reaction proceeds at the desired rate.

Finally, the program includes code to finalize the reaction by slowing down the agitator speed and raising the temperature of the reactor for a set period of time. These values can be adjusted as needed to meet the specific requirements of the production process.


***

Exported on March 11, 2023 10:56 PM.