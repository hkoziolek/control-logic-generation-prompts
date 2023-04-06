# ISA 88 Recipe for PVC

**Human:**
give an isa 88 control recipe of batch production of polyvinylchloride by polymerization of vinylchloride monomers. The process consists of one or more process stages which are organized as an ordered set,
which can be serial, parallel, or both. A process stage is a part of a process that usually operates independently from other process stages. It usually results in a planned sequence of
chemical or physical changes in the material being processed. The recpie should contain at least the following stages: polymerize, Decover, Dry. Each process stage consists of an ordered set of one or more process operations. Process
operations represent major processing activities. A process operation usually results in a chemical or physical change in the material being processed. Control recpie should contain at least the following operations: Prepare reactor: Evacuate the reactor to remove oxygen. Charge: Add demineralized water and surfactants. React: Add vinyl chloride monomer and catalyst, heat to 55 - 60°C, and hold at this temperature until the reactor pressure decreases. Each process operation can be subdivided into an ordered set of one or more process actions that carry out the processing required by the process operation. Process actions describe minor processing activities that are combined to make up a process operation. Typical process actions for the react process operation might be the following:
— Add: Add the required amount of catalyst to the reactor. — Add: Add the required amount of vinyl chloride monomer to the reactor. — Heat: Heat the reactor contents to 55 - 60°C. — Hold: Hold the reactor contents at 55 - 60°C until the reactor pressure decreases.

***

**Assistant:**

Here is an example ISA 88 control recipe for batch production of polyvinylchloride by polymerization of vinylchloride monomers:

Process Stage 1: Polymerize

Process Operation 1: Prepare reactor
1.1 Evacuate the reactor to remove oxygen

Process Operation 2: Charge
2.1 Add demineralized water
2.2 Add surfactants

Process Operation 3: React
3.1 Add vinyl chloride monomer
3.2 Add catalyst
3.3 Heat to 55-60°C
3.4 Hold at 55-60°C until reactor pressure decreases

Process Stage 2: Decover

Process Operation 1: Decover
1.1 Cool reactor to below 40°C
1.2 Open reactor and release unreacted vinyl chloride monomer
1.3 Remove polymer product

Process Stage 3: Dry

Process Operation 1: Dry
1.1 Transfer polymer product to a dryer
1.2 Dry polymer product to desired moisture content

Each process operation can be further subdivided into process actions, as described in the question. The ISA 88 control recipe provided here is just an example and may need to be modified based on the specific requirements of the polyvinylchloride production process.


***

**Human:**
descirbe stage 3.4 as a self contained iec 61131-3 st program.

***

**Assistant:**

Stage 3.4 "Hold at 55-60°C until reactor pressure decreases" can be implemented as a self-contained IEC 61131-3 structured text program.

Here is an example implementation of Stage 3.4 as an IEC 61131-3 structured text program:

```
PROGRAM STAGE_3_4
VAR
   reactor_pressure : REAL;      (* pressure in the reactor *)
   hold_time : TIME := t#60s;    (* hold time, set to 60 seconds *)
END_VAR

(* Main program *)
WHILE reactor_pressure > 0.0 DO
   (* Read current reactor pressure *)
   reactor_pressure := READ_REACTOR_PRESSURE();

   (* Hold at 55-60°C until reactor pressure decreases *)
   IF reactor_pressure > 0.0 THEN
      HOLD_AT_TEMPERATURE(55.0, 60.0, hold_time);
   END_IF
END_WHILE

(* Subroutines *)
FUNCTION_BLOCK READ_REACTOR_PRESSURE
   VAR_INPUT
      (* Input variables *)
   END_VAR
   VAR_OUTPUT
      (* Output variables *)
      reactor_pressure : REAL;   (* pressure in the reactor *)
   END_VAR
BEGIN
   (* Read the current pressure from the reactor *)
   reactor_pressure := READ_PRESSURE_SENSOR();
END_FUNCTION_BLOCK

FUNCTION_BLOCK HOLD_AT_TEMPERATURE
   VAR_INPUT
      (* Input variables *)
      min_temperature : REAL;    (* minimum temperature for holding *)
      max_temperature : REAL;    (* maximum temperature for holding *)
      hold_time : TIME;          (* hold time *)
   END_VAR
BEGIN
   (* Set the temperature to the desired range *)
   SET_TEMPERATURE(min_temperature, max_temperature);

   (* Wait for the specified hold time *)
   WAIT(hold_time);

   (* Reset the temperature to ambient *)
   RESET_TEMPERATURE();
END_FUNCTION_BLOCK

```

In this program, the `READ_REACTOR_PRESSURE` function block reads the current pressure in the reactor, and the `HOLD_AT_TEMPERATURE` function block sets the temperature to the desired range and waits for the specified hold time before resetting the temperature to ambient. The main program loops while the reactor pressure is greater than 0.0 and calls the `HOLD_AT_TEMPERATURE` function block to maintain the desired temperature until the pressure decreases.

This IEC 61131-3 structured text program can be integrated into a larger control system that implements the ISA 88 control recipe for batch production of polyvinylchloride by polymerization of vinylchloride monomers.


***

Exported on March 12, 2023 9:44 PM.