# Control Logic Generation Prompt Collection

The following 100 prompts are designed to test the ability of LLMs to support control engineers in industrial automation. They are structured in 10 categories. Many of them generate IEC 61131-3 Structured Text as a typical control programming language. Below each prompt is the answer we obtained from ChatGPT with GPT-4.

## Standard Algorithms

### Counter:

Write a self-contained function block in 61131-3 structured text that implements a counter.<br>[ChatGPT Answer](<../chatgpt/Counter.md>)

### Fahrenheit to Celsius:

Write a self-contained function block in 61131-3 structured text that converts fahrenheit to celsius.<br>[ChatGPT Answer](<../chatgpt/Fahrenheit to Celsius.md>)

### Real Comperator:

Write a self-contained function block in 61131-3 structured text that compares two real inputs up to n digits.<br>[ChatGPT Answer](<../chatgpt/Real Comperator.md>)

### Timer:

Write a self-contained function block in 61131-3 structured text that implements a timer.<br>[ChatGPT Answer](<../chatgpt/Timer.md>)

### DecToHex:

Write a self-contained function block in 61131-3 structured text that converts a 10 digit decimal value to hexadecimal.<br>[ChatGPT Answer](<../chatgpt/DecToHex.md>)

### PID Controller:

Write a self-contained function block in 61131-3 structured text that implements a PID controller.<br>[ChatGPT Answer](<../chatgpt/PID Controller.md>)

### Binary Search:

Write a self-contained function block in 61131-3 structured text that implements a binary search to find an integer in an array of 100 integers.<br>[ChatGPT Answer](<../chatgpt/Binary Search.md>)

### Kalman Filter:

Write a self-contained function block in IEC 61131-3 Structured Text that implements a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. <br>[ChatGPT Answer](<../chatgpt/Kalman Filter.md>)

### Quicksort:

Write a self-contained function block in 61131-3 that implements the quicksort algorithm. <br>[ChatGPT Answer](<../chatgpt/Quicksort.md>)

### Heapsort:

Write a self-contained function block in IEC 61131-3 to implement the heapsort algorithm. Do not used recursion as this is disallowed in 61131-3. Do not used keyword 'DOWNTO' in for loops.<br>[ChatGPT Answer](<../chatgpt/Heapsort.md>)

## Mathematical Functions

### Matrix Multiplication:

Write a self-contained function block in 61131-3 to multiply two 4 by 4 matrices.<br>[ChatGPT Answer](<../chatgpt/Matrix Multiplication.md>)

### Sine Function:

Write a self-contained function block in IEC 61131-3 Structured Text to compute a sine function.<br>[ChatGPT Answer](<../chatgpt/Sine Function.md>)

### Natural Logarithm:

Write a self-contained function block in IEC 61131-3 Structured Text to compute a natural logarithm.<br>[ChatGPT Answer](<../chatgpt/Natural Logarithm.md>)

### Mean and StdDev:

Write a self-contained function block in IEC 61131-3 Structured Text to compute the mean and standard deviation for a input array of 100 integers.<br>[ChatGPT Answer](<../chatgpt/Mean and StdDev.md>)

### Fast Fourier Transform:

Write a self-contained function block in IEC 61131-3 Structured Text to compute Fast Fourier Transform.<br>[ChatGPT Answer](<../chatgpt/Fast Fourier Transform.md>)

### Eigenvalue:

Write a self-contained function block in IEC 61131-3 Structured Text to compute the eigenvalue of 10 by 10 matrix. <br>[ChatGPT Answer](<../chatgpt/Eigenvalue.md>)

### Linear Interpolation:

Write a self-contained function block in IEC 61131-3 Structured Text to compute a linear interpolation.<br>[ChatGPT Answer](<../chatgpt/Linear Interpolation.md>)

### Spline Interpolation:

Write a self-contained function block in IEC 61131-3 Structured Text to compute a spline interpolation. <br>[ChatGPT Answer](<../chatgpt/Spline Interpolation.md>)

### Poisson Distribution:

Write a self-contained function block in 61131-3 to compute a Poisson distribution.<br>[ChatGPT Answer](<../chatgpt/Poisson Distribution.md>)

### Linear Programming:

Write a self-contained function block in 61131-3 for linear programming.<br>[ChatGPT Answer](<../chatgpt/Linear Programming.md>)

## PLC Programming Exercises

### Conveyor Control:

Write a self-contained 61131-3 structured text program, not a function block, to control a conveyor belt system with three stations, which each allow as user to stop the conveyor. The system should automatically start and stop based on five sensors that detect the presence of objects on the conveyor belt. The conveyor belt speed shall be maintained at 2 meters per second.<br>[ChatGPT Answer](<../chatgpt/Conveyor Control.md>)

### Heating Control:

Write a self-contained 61131-3 structured text program, not a function block, to control the temperature of a heating system. The system should automatically turn on and off based on three temperature sensors and maintain a constant temperature range between 20 and 22 degree celsius.<br>[ChatGPT Answer](<../chatgpt/Heating Control.md>)

### Traffic Control:

Write a self-contained 61131-3 structured text program, not a function block,  to control a traffic light system. The system shall react to pedestrian push buttons and to the presence of emergency vehicles to give them priority.<br>[ChatGPT Answer](<../chatgpt/Traffic Control.md>)

### Pneumatic Control:

Write a self-contained 61131-3 structured text program, not a function block, to control a pneumatic system with a control loop frequency of 100 ms. The system should control the flow of air to actuators based on input signals to 50 standard liters per minute, and maintain a pressure range of 5.5 to 6 bar.<br>[ChatGPT Answer](<../chatgpt/Pneumatic Control.md>)

### Elevator Control:

Write a self-contained 61131-3 structured text program for controlling an elevator. Every floor of the 5-floor building contains bottom and top limit switches. There is a 7 seconds timer for opening the elevator door, and a 10 seconds timer for opening the door again if none of the buttons inside the elevator cabin are pressed. The elevator operates based on the current direction and the direction imposed by up and call buttons on each floor.<br>[ChatGPT Answer](<../chatgpt/Elevator Control.md>)

### Car Wash Station:

Write a PLC program in ST according to IEC 61131-3, to create an automatic car wash station with only one station. Station detect if car is there by a sensor and if no human is present (In car wash area) then it start to wash to car. If there is any human detected in the car wash area then car wash station should stop and send an alarm.<br>[ChatGPT Answer](<../chatgpt/Car Wash Station.md>)

### Underground Car Park:

Write a PLC program in ST according to IEC 61131-3, to create an Entry/Exit Control of the Underground Car Park. 

These are sensors in the system:
X1: Photoelectric switch at the ground floor entry/exit. X1 will be ON when a car passes.
X2: Photoelectric switch at the basement entry/exit. X2 will be ON when a car passes.
M1: M1 will be ON for one scan cycle when a car from the ground floor passes X1.
M2: M2 will be ON for one scan cycle when a car from the basement passes X1.
M3: M3 will be ON for one scan cycle when a car from the basement passes X2.
M4: M4 will be ON for one scan cycle when a car from the ground floor passes X2.

Intermidiate variables:
M20: M20 = ON during the process of a car entering the passage from the ground floor.
M30: M30 = ON during the process of a car entering the passage from the basement.

These are outputs devices in the system:
Y1: Red lights at the entry/exit of the ground floor and the basement.
Y2: Green lights at the entry/exit of the ground floor and the basement.

Description of the process: 
"The entry/exit of the underground car park is a single lane passage which needs the traffic lights to control the cars. Red lights prohibit cars entering or leaving while green lights allowcars to enter or leave. When a car enters the passage from the entry of the ground floor, the red lights both on the ground floor and the basement will be ON, and the green lights will be OFF. Any car entering or leaving is prohibited during the process till the car passes through the passage completely. When the passage is clear, the green lights will be ON again and allow other cars entering from the ground floor or the basement.Similarly, when a car leaves the basement and enters the passage, any other car entering or leaving is prohibited till the car passes from the passage to the ground completely.When PLC runs, the initial setting of traffic lights will be green lights ON and red lights OFF." <br>[ChatGPT Answer](<../chatgpt/Underground Car Park.md>)

### Pick and Place:

Write a PLC program in ST according to IEC 61131-3, for a pick-and-place application for a robot with two conveyors.
Here is the description of the process:
1) Whole machine has two modes: auto and manual
2) Manual Mode: When the button Manual is pressed, the robotic arm will begin to execute the manual control process: pressing Clip to clip the product from conveyor A, pressing Transfer to move the product to conveyor B, and pressing Release to release the product and send it away by conveyor B.
3) Auto Mode: When the button Auto is pressed, the robotic arm will begin to execute the auto control process once: clip the product (keep holding this product before releasing it), then transfer the product (the action takes 2 seconds), and then lastly release the product. The auto control process can be performed one more time if the button Auto is pressed again.
4) Manual control process and auto control process are interlocked.<br>[ChatGPT Answer](<../chatgpt/Pick and Place.md>)

### Empty Bottle Removal:

Write a self-contained 61131-3 structured text program for packaging bottles. After filling, the bottles are moved with a conveyor to packaging. A proximity sensor detects any bottle, another one only empty bottles. A cylinder removes empty bottles.<br>[ChatGPT Answer](<../chatgpt/Empty Bottle Removal.md>)

### Coffee Maker:

Write a self-contained 61131-3 structured text program for a coffee machine.

This machine contains three tanks, each for coffee, milk, and mixer, and three valves, one for the coffee, one for the milk, and the last valve for the output. This coffee machine contains a mixer, which is required to mix the coffee and milk properly to create the best output, The mixer is designed to work for four seconds after which it will automatically stop and the output valve will open to get the output.

The mixer is designed with a timer and will automatically start when the mixer tank reaches the maximum level, the tank is attached to the mixer as both the valves of coffee and milk are open and it started to fill the mixer and then the tank level comes into play with the preset maximum level, the mixer tank can be filled up to 130ml as it reaches the maximum level, the valves of coffee and milk will close and then it will start the mixing.

The coffee machine contains four Push buttons. Button one is for emergency stop, Button two is to start the machine, Button three is for Coffee and Milk and the last button is for Coffee only. The emergency stop is use as a safety button if anything goes wrong in the machine like if any of the valves not open, if the tank level does not work properly, if the mixer fails to work properly or any of the unexpected events occur, then there is a need of emergency stop to stop the machine instantly. <br>[ChatGPT Answer](<../chatgpt/Coffee Maker.md>)

## Process Control

### PID Temperature Control Gas Turbine:

Write a self-contained IEC 61131-3 Structured Text program to implement PID feedback control for the temperature inside a gas turbine by providing a setpoint for the opening of an inlet valve. <br>[ChatGPT Answer](<../chatgpt/PID Temperature Control Gas Turbine.md>)

### PID Level Control Distillation Column:

Write a self-contained IEC 61131-3 Structured Text program to implement PID feedback control for the level in a distillation column. The output signal goes to an inlet valve feeding the column.<br>[ChatGPT Answer](<../chatgpt/PID Level Control Distillation Column.md>)

### PID Pressure Control Chemical Reactor:

Write a self-contained 61131-3 structured text program to implement PID feedback control for the pressure in a chemical reactor.<br>[ChatGPT Answer](<../chatgpt/PID Pressure Control Chemical Reactor.md>)

### PID Flow Control Water Treatment:

Write a self-contained 61131-3 structured text program to implement PID feedback flow control for the chemical dosing in a water treatment process. Assume a dosing rate of 3 ppm for chlorine and a sampling rate of 100 ms.<br>[ChatGPT Answer](<../chatgpt/PID Flow Control Water Treatment.md>)

### PID ph Control:

Write a self-contained 61131-3 structured text program, not a function block, to implement PID feedback ph control.<br>[ChatGPT Answer](<../chatgpt/PID ph Control.md>)

### Feedforward Control Mixing:

Write a self-contained 61131-3 structured text program, not a function block, to implement feedforward control for mixing two reactants. <br>[ChatGPT Answer](<../chatgpt/Feedforward Control Mixing.md>)

### Feedforward Control Conveyor:

Write a self-contained 61131-3 structured text program, not a function block, to implement feedforward control for adjusting the speed of a conveyor belt based on sensor-based predicted load.<br>[ChatGPT Answer](<../chatgpt/Feedforward Control Conveyor.md>)

### Cascade Control Heat Exchanger:

Write a self-contained 61131-3 structured text program, not a function block, to implement cascade control for the temperature in a heat exchanger.<br>[ChatGPT Answer](<../chatgpt/Cascade Control Heat Exchanger.md>)

### Cascade Control Oil Refinery:

Write a self-contained 61131-3 structured text program, not a function block, to implement cascade control for the pressure in an oil refinery. The primary loop controls the pressure in the vessel, while the secondary loop controls the flow of oil into the vessel. The output of the primary loop is used as the setpoint for the secondary loop.<br>[ChatGPT Answer](<../chatgpt/Cascade Control Oil Refinery.md>)

### Ratio Control Mixing:

Write a self-contained 61131-3 structured text program, not a function block, to implement ratio control for mixing two reactants in a 2 to 1 ratio.<br>[ChatGPT Answer](<../chatgpt/Ratio Control Mixing.md>)

## Sequential Control

### Batch Polyethylene:

Write a self-contained 61131-3 structured text program, not a function block, to implement batch control for a polyethylene production process. It shall contain the steps raw material preparation, polymerization, quenching, drying, pelletizing, quality control, as well as packaging and storage.<br>[ChatGPT Answer](<../chatgpt/Batch Polyethylene.md>)

### Batch PVC:

Create an ISA-88 control recipe for batch production of polyvinylchloride by polymerization of vinylchloride monomers. The recipe should contain at least the following stages: polymerize, decover, dry. Each process stage consists of an ordered set of one or more process operations. 
The control recipe should contain at least the following operations: 
	- Prepare reactor: Evacuate the reactor to remove oxygen. 
	- Charge: Add demineralized water and surfactants. 
	- React: Add vinyl chloride monomer and catalyst, heat to 55 - 60�C, and hold at this temperature until the reactor pressure decreases. 

Write a self-contained 61131-3 structured text program for the sequential control of the reactor including concrete process parameters and timers.

Provide the content for the EvacuateReactor method.
Provide the content for the AddDemineralizedWater method.<br>[ChatGPT Answer](<../chatgpt/Batch PVC.md>)

### Batch Adhesive:

Create an ISA-88 batch control recipe for adhesive production. 

Write a self-contained 61131-3 structured text program for the sequential control in step B.2 Reaction. Include concrete process parameters and timers.

Add the control logic that actually calls these methods.<br>[ChatGPT Answer](<../chatgpt/Batch Adhesive.md>)

### Batch Urea Fertilizer:

Create an ISA-88 batch control recipe of urea fertilizer production.

Write a self-contained 61131-3 structured text program for the sequential control of the reaction stage with typical parameter values.

Narrow down the code for heating, cooling, and pressure regulation.<br>[ChatGPT Answer](<../chatgpt/Batch Urea Fertilizer.md>)

### Batch Aspirin:

Create an ISA-88 control recipe of a batch production for aspirin known as acetylsalicylic acid. The physical structure consists of a reactor, a crystallizer, a centrifuge and a dryer. Educts are Acetic anhydride, Salicylic acid, and  sulphuric acid as catalyst. Products are acetylsalicylic acid and acetic acid. Drying should happen at 90 �C.

Write a self-contained 61131-3 structured text program for the sequential control of the reaction stage with typical parameter values.<br>[ChatGPT Answer](<../chatgpt/Batch Aspirin.md>)

### Batch Cocoa Milk:

Create an ISA-88 batch recipe for 100kg cocoa milk production. Ingredients should include milk, water, liquid sugar and cocoa. Equipment consists of a mixing and blending vessel able to stir and heat. Provide adequate amounts and temperatures.

Write a self-contained 61131-3 structured text program for the sequential control of the mixing with typical parameter values.<br>[ChatGPT Answer](<../chatgpt/Batch Cocoa Milk.md>)

### 3D Pouch Making Machine:

A 3D pouch making machine has 8 heating and 8 cooling station. It has one horizontal and one vertical cutter at the end of the machine. The machine has two feeder units to feed raw material where winding tension is very important to maintain on order to keep proper tension in the raw material through out the machine. Create a detailed start-up and shutdown sequence for this machine and formulate it as IEC 61131-3 Structured Text.<br>[ChatGPT Answer](<../chatgpt/3D Pouch Making Machine.md>)

### Startup Steam Generator:

Write a non-linear model-predictive controller in Python that optimizes the startup of a steam generator in a power plant.<br>[ChatGPT Answer](<../chatgpt/Startup Steam Generator.md>)

### Shutdown Steel Production:

Create a list of steps for the controlled shut-down of a steel production facility.

Create a concrete control narrative for steps 4 to 6 including concrete ranges and setpoints.

Write a self-contained IEC 61131-3 structured text program according to this control narrative.

Write a self-contained IEC 61131-3 function for gradually reducing the fuel gas flow rate to the furnace burners over a period of 12 hours.

Write a self-contained IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a fuel-to-air ratio of 1:2.5 during the shutdown process.<br>[ChatGPT Answer](<../chatgpt/Shutdown Steel Production.md>)

### Startup Paper Machine:

Create a detailed startup sequence for the press section of a Valmet paper machine including typical parameter values.

Write a self-contained IEC 61131-3 structured text program to control this startup sequence.<br>[ChatGPT Answer](<../chatgpt/Startup Paper Machine.md>)

## Interlocks

### IL Overfill Protection:

Write a 61131-3 structured text program to implement an interlock to provide overfill of a vessel using a level sensor and and inlet valve.<br>[ChatGPT Answer](<../chatgpt/IL Overfill Protection.md>)

### IL Pressure Relieve:

Write a 61131-3 structured text program to implement an interlock to open a pressure relieve valve in a vessel upon overpressure.<br>[ChatGPT Answer](<../chatgpt/IL Pressure Relieve.md>)

### IL Distillation Column:

Create a P&I diagram in textual notation for a distillation column including process equipment, instrumentation, control functions, safety interlocks, and piping, Use typical tagnames.

Write a 61131-3 structured text program to implement the interlocks of this distillation column. Provide concrete values for the high limits and low limits.<br>[ChatGPT Answer](<../chatgpt/IL Distillation Column.md>)

### IL Cause Effect Matrix:

Create a cause & effect matrix for interlocks required for a chemical reactor. Each line shall contain a different cause related to a sensor value, and each column shall contain a different effect related to a corresponding actuator action.<br>[ChatGPT Answer](<../chatgpt/IL Cause Effect Matrix.md>)

### IL Motor Function Block Diagram:

Create a motor interlock as a function block diagram that ensures that a motor is not started while equipment is still running.

Provide the content of the Motor Interlock function block as a 61131-3 structured text function block.<br>[ChatGPT Answer](<../chatgpt/IL Motor Function Block Diagram.md>)

### IL Extended Cause Effect Matrix:

Create an extended cause & process action matrix for the interlocks for a chemical reactor. The column headings shall be the safety actions performed using the actuators in the system.<br>[ChatGPT Answer](<../chatgpt/IL Extended Cause Effect Matrix.md>)

### IL Gas Wellhead:

Write a 61131-3 structured text program to implement emergency interlocks for a subsea gas wellhead.<br>[ChatGPT Answer](<../chatgpt/IL Gas Wellhead.md>)

### IL Safety Doors:

Write a 61131-3 structured text program to implement interlocks for safety doors in a chemical reactor.<br>[ChatGPT Answer](<../chatgpt/IL Safety Doors.md>)

### IL Prilling Station:

Provide a complete list of interlocks required for a prilling station for ammonium nitrates.<br>[ChatGPT Answer](<../chatgpt/IL Prilling Station.md>)

### IL Gas Turbine:

Provide a complete list of interlocks required for a gas turbine in a power plant.<br>[ChatGPT Answer](<../chatgpt/IL Gas Turbine.md>)

## Diagnostics / Communication

### Modbus Server:

Write a self-contained 61131-3 structured text function block to act as a Modbus server. It shall process up to 10 parallel client connection requests by Modbus TCP. Modbus requests work within data ranges that map the input and holding registers. The following Modbus function codes are supported:
0x01 Read Coils
0x02 Read Discrete Inputs
0x03 Read Holding Registers
0x04 Read Input Registers
0x05 Write Single Coil
0x06 Write Single Register
0x0F Write Multiple Coils
0x10 Write Multiple Registers
0x17 Read/Write Multiple Registers

Provide the content of the ReadCoils method.<br>[ChatGPT Answer](<../chatgpt/Modbus Server.md>)

### Profinet DP Diagnostics:

Write a self-contained 61131-3 structured text function block that reads diagnostic data from a Profibus DP slave device.<br>[ChatGPT Answer](<../chatgpt/Profinet DP Diagnostics.md>)

### IO-Link Reading value:

Give me a function block written in ST (based on IEC 61131) to read 5 values from remote IO-Link master along with status of operation.<br>[ChatGPT Answer](<../chatgpt/IO-Link Reading value.md>)

### CANOpen PDO Registration:

Give me a IEC 61131 based ST function block  "CAN_REGISTER_COBID" which is used to register a PDO or a CAN Layer 2 message for reception by the network layer or to delete such a registration. When calling the block with input REGISTER set to TRUE, the specified COBID (CAN identifier) for receiving messages in the network layer is registered. When calling with REGISTER = FALSE, registry of the respective COBIDs is deleted again. Calling the block with REGISTER = FALSE and COBID = 0 deletes all registries and all the messages stored in the buffer of the network layer.<br>[ChatGPT Answer](<../chatgpt/CANOpen PDO Registration.md>)

### Profibus Diagnostics:

Write a self-contained 61131-3 structured text program to retrieve diagnostic data from a Profibus device using the Profibus DPV1 protocol. Add a CASE statement to handle 10 types of this diagnostic data.

Refine the code to use concrete diagnostic data types.<br>[ChatGPT Answer](<../chatgpt/Profibus Diagnostics.md>)

### OPC UA Subscription Create:

Write C-code for a Function block to be wrapped inside IEC 61131-3 Structured Text code. The function block shall create an OPC UA subscription using the Open62541 library using a provided Connection Handle as DWORD. As input it also gets an executed flag (type BOOL), a priority (BYTE) and a timeout (TIME). As output it provides three flags Done, Busy, Error, as well as two DWORDs ErrorID and SubscriptionHdl. As an IN/OUT variable the function block has a PublishingInterval (TIME). 

Explain how to wrap this function block into IEC 61131-3 structured text and provide an example for calling it.<br>[ChatGPT Answer](<../chatgpt/OPC UA Subscription Create.md>)

### EtherCAT State Machine:

Write a IEC 61131-3 ST program to go through all states of an EtherCAT slave device using the ESM function block. Use the typical statenames instead of numbers and only perform state changes if they are allowed. Add a 5 second timer delay before each state transititon.<br>[ChatGPT Answer](<../chatgpt/EtherCAT State Machine.md>)

### OPC UA Client:

Write c-code for OPC UA Client and then wrap it to a IEC 61131 based function block written in ST. Function block should have inputs pin as Execute (bool), ServerUrl (as STRING[255] ), Timeout (Time), and output pins Done (Bool), Busy (bool), Error (Bool) and ErrorID (DWORD).<br>[ChatGPT Answer](<../chatgpt/OPC UA Client.md>)

### Communication Monitoring:

Give me a function block written in ST as per IEC 61131-3, which monitors communication connection to OPC UA Server, Modebus Server, and Profinet used in a machine and create alarm if one of them is down. Please also added entry in audit trail reason of server down along with its error code.<br>[ChatGPT Answer](<../chatgpt/Communication Monitoring.md>)

### Ethernet PowerLink diagnostic :

Write an IEC 61131 based function block in ST to get Ethernet PowerLink diagnostic information of a control node device from a controller ( Powerlink managing node).<br>[ChatGPT Answer](<../chatgpt/Ethernet PowerLink diagnostic .md>)

## Advanced Process Control

### MPC Matlab Distillation Column:

Write MATLAB code to implement an example mathematical model for a distillation column, which describes its dynamics and the relationships between feed rates and temperature. Do not plot the results.

Write MATLAB code to implement a model-predictive control scheme using this mathematical model for the distillation column.<br>[ChatGPT Answer](<../chatgpt/MPC Matlab Distillation Column.md>)

### MPC Matlab Aircraft Trajectory:

Write MATLAB code to implement model-predictive control to optimize the trajectory of a aircraft.<br>[ChatGPT Answer](<../chatgpt/MPC Matlab Aircraft Trajectory.md>)

### MPC Python Turbine:

Write Python code to implement model-predictive control for a turbine in a thermal power plant.<br>[ChatGPT Answer](<../chatgpt/MPC Python Turbine.md>)

### MPC Python Robot Movement:

Write Python code to implement model-predictive control for a optimizing a robot movement.<br>[ChatGPT Answer](<../chatgpt/MPC Python Robot Movement.md>)

### MPC Python Cellulose Fiber:

How can a model predictive control help in Cellulose fibers production from wood, where the infeed and outfeed must operate continuously while the material between undergoes a two-stage batch process?
Supplied at a average rate of 50 tons per hour, the material must first be pre-treated in a reactor and then homogenized before being transported into a 1,000 cubic meter tank. The preliminary product is not taken from this buffer tank at a constant rate, but rather on demand. To minimize the risk of downtime in downstream stations, a constantly high fill level must be maintained. Due to the duration of the upstream batch processes, however, it takes around two hours to react to a fluctuations in demand. This dead time ruled out the use of a PID controller to automate flow rate adjustments.


Write Python code to simulate the dynamics of such a system. 

Write Python code to implement model-predictive control for this system.<br>[ChatGPT Answer](<../chatgpt/MPC Python Cellulose Fiber.md>)

### MPC CPlusPlus Wind Farm:

Write C++ code to implement model-predictive control for a wind farm.<br>[ChatGPT Answer](<../chatgpt/MPC CPlusPlus Wind Farm.md>)

### MPC CPlusPlus HVAC:

Write C++ code to implement model-predictive control for an HVAC system.<br>[ChatGPT Answer](<../chatgpt/MPC CPlusPlus HVAC.md>)

### Fuzzy Logic Control Chemical Reactor:

Write Python code for fuzzy logic control of a chemical reactor.<br>[ChatGPT Answer](<../chatgpt/Fuzzy Logic Control Chemical Reactor.md>)

### ANN Control Chemical Reactor:

Write Python code for using artificial neural networks for advanced process control of the  temperature in a chemical reactor.<br>[ChatGPT Answer](<../chatgpt/ANN Control Chemical Reactor.md>)

### SPC Steel Manufacturing:

Write Python code for statistical process control in steel manufacturing.<br>[ChatGPT Answer](<../chatgpt/SPC Steel Manufacturing.md>)

## Various Engineering Inputs

### Control Narrative Ammonium Nitrate:

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.<br>[ChatGPT Answer](<../chatgpt/Control Narrative Ammonium Nitrate.md>)

### Control Narrative Ethanol Production:

Create a control narrative for ethanol production including concrete setpoints and ranges.

Create a detailed explanation of each control step during Fermentation. Create one paragraph per subsection in Section 3.<br>[ChatGPT Answer](<../chatgpt/Control Narrative Ethanol Production.md>)

### Control Narrative Beer Brewing:

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.<br>[ChatGPT Answer](<../chatgpt/Control Narrative Beer Brewing.md>)

### IO List Steam Water Cycle:

Create an I/O list as a table for feedwater control in a steam-water cycle in a power plant. Have as columns names, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.<br>[ChatGPT Answer](<../chatgpt/IO List Steam Water Cycle.md>)

### IO List Rolling Mill:

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.<br>[ChatGPT Answer](<../chatgpt/IO List Rolling Mill.md>)

### P-ID Steam Water Cycle:

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.<br>[ChatGPT Answer](<../chatgpt/P-ID Steam Water Cycle.md>)

### SCD LNG Vaporizer:

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.<br>[ChatGPT Answer](<../chatgpt/SCD LNG Vaporizer.md>)

### PFD Penicillin Fermentation:

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.<br>[ChatGPT Answer](<../chatgpt/PFD Penicillin Fermentation.md>)

### FBD PID:

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.<br>[ChatGPT Answer](<../chatgpt/FBD PID.md>)

### SFC Traffic Light:

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.<br>[ChatGPT Answer](<../chatgpt/SFC Traffic Light.md>)

## Programmer Support

### Fix Traffic Light Code:

Can you find the error in the following 61131-3 ST code:
PROGRAM TrafficLightControl
VAR
    pedestrianButtonPressed: BOOL;
    emergencyVehicleApproaching: BOOL;
    greenLightOn: BOOL;
    yellowLightOn: BOOL;
    redLightOn: BOOL;
    timer: TON; // timer to control the duration of green and yellow lights
END_VAR

// Initialize the program
greenLightOn := TRUE;
yellowLightOn := FALSE;
redLightOn := FALSE;
timer(IN := NOT emergencyVehicleApproaching, PT := T#5s);

// Main program loop
WHILE TRUE DO
    // Check for pedestrian button press
    pedestrianButtonPressed := ReadPedestrianButton();

    // Check for emergency vehicle approaching
    emergencyVehicleApproaching := ReadEmergencyVehicleSensor();

    IF emergencyVehicleApproaching THEN
        // Turn off all lights and turn on green light for emergency vehicle
        greenLightOn := TRUE;
        yellowLightOn := FALSE;
        redLightOn := FALSE;
        timer(IN := FALSE);

    ELSEIF pedestrianButtonPressed THEN
        // Turn off all lights and turn on red light and pedestrian light
        greenLightOn := FALSE;
        yellowLightOn := FALSE;
        redLightOn := TRUE;
        timer(IN := FALSE);

        // Wait for pedestrian to cross
        WAIT UNTIL NOT pedestrianButtonPressed;

        // Turn on yellow light for warning and start the timer
        yellowLightOn := TRUE;
        redLightOn := FALSE;
        timer(IN := NOT emergencyVehicleApproaching);

    ELSE
        // Check the timer and switch to the next light if it's time
        IF timer.Q THEN
            IF greenLightOn THEN
                greenLightOn := FALSE;
                yellowLightOn := TRUE;
                timer(IN := NOT emergencyVehicleApproaching);

            ELSEIF yellowLightOn THEN
                yellowLightOn := FALSE;
                redLightOn := TRUE;
                timer(IN := FALSE);

            ELSE // red light is on
                redLightOn := FALSE;
                greenLightOn := TRUE;
                timer(IN := NOT emergencyVehicleApproaching);
            END_IF;
        END_IF;
    END_IF;

    // Set the traffic lights based on the variables
    SetTrafficLights(greenLightOn, yellowLightOn, redLightOn);

    // Wait for a short time before checking again
    DELAY 100ms;
END_WHILE

// Read the pedestrian button state from an input
FUNCTION ReadPedestrianButton: BOOL
    // Code to read the input goes here
END_FUNCTION

// Read the emergency vehicle sensor state from an input
FUNCTION ReadEmergencyVehicleSensor: BOOL
    // Code to read the input goes here
END_FUNCTION

// Set the traffic lights based on the variables
PROCEDURE SetTrafficLights(
    green: BOOL;
    yellow: BOOL;
    red: BOOL
)
    // Code to set the traffic lights goes here
END_PROCEDURE<br>[ChatGPT Answer](<../chatgpt/Fix Traffic Light Code.md>)

### Explain Cascade Control Code:

Explain the following code:
PROGRAM CascadeControl
VAR
    // Primary loop variables
    PV1: REAL; // Process variable: vessel pressure
    SP1: REAL; // Setpoint: target pressure
    OP1: REAL; // Output: secondary loop setpoint
    Kp1: REAL := 1.0; // Proportional gain
    Ki1: REAL := 0.1; // Integral gain
    Kd1: REAL := 0.05; // Derivative gain
    e1, e1_prev, e1_sum, e1_diff: REAL;

    // Secondary loop variables
    PV2: REAL; // Process variable: flow rate
    SP2: REAL; // Setpoint: target flow rate (OP1)
    OP2: REAL; // Output: control valve position
    Kp2: REAL := 2.0; // Proportional gain
    Ki2: REAL := 0.2; // Integral gain
    Kd2: REAL := 0.1; // Derivative gain
    e2, e2_prev, e2_sum, e2_diff: REAL;

    dt: TIME := t#100ms; // Sample time
    t_last: TIME;
END_VAR

METHOD RunCascadeControl
    // Read current pressure and flow rate values
    PV1 := ReadPressure();
    PV2 := ReadFlowRate();

    // Primary loop: pressure control
    e1 := SP1 - PV1;
    e1_sum := e1_sum + e1 * dt;
    e1_diff := (e1 - e1_prev) / dt;
    OP1 := Kp1 * e1 + Ki1 * e1_sum + Kd1 * e1_diff;
    e1_prev := e1;

    // Limit OP1 to a valid range
    IF OP1 > 100.0 THEN
        OP1 := 100.0;
    ELSIF OP1 < 0.0 THEN
        OP1 := 0.0;
    END_IF;

    // Secondary loop: flow control
    SP2 := OP1;
    e2 := SP2 - PV2;
    e2_sum := e2_sum + e2 * dt;
    e2_diff := (e2 - e2_prev) / dt;
    OP2 := Kp2 * e2 + Ki2 * e2_sum + Kd2 * e2_diff;
    e2_prev := e2;

    // Limit OP2 to a valid range
    IF OP2 > 100.0 THEN
        OP2 := 100.0;
    ELSIF OP2 < 0.0 THEN
        OP2 := 0.0;
    END_IF;

    // Set control valve position
    SetValvePosition(OP2);
END_METHOD

END_PROGRAM
<br>[ChatGPT Answer](<../chatgpt/Explain Cascade Control Code.md>)

### Generate Documentation Urea Reaction:

Generate a developer documentation for the following code:
PROGRAM UreaReactionControl
VAR
    // Inputs
    stAmmoniaValve : BOOL; // TRUE when ammonia valve is open
    stCO2Valve : BOOL; // TRUE when CO2 valve is open
    rCurrentPressure : REAL;
    rCurrentTemperature : REAL;

    // Outputs
    stAmmoniaValveControl : BOOL; // TRUE to open ammonia valve
    stCO2ValveControl : BOOL; // TRUE to open CO2 valve

    // Internal variables
    stStep1 : BOOL := FALSE; // Load raw materials
    stStep2 : BOOL := FALSE; // Control reaction
    stReactionFinished : BOOL := FALSE; // Reaction finished flag

    // Parameters
    rTargetPressure : REAL := 175.0; // Target reactor pressure in bars
    rPressureTolerance : REAL := 5.0; // Pressure tolerance in bars
    rTargetTemperature : REAL := 185.0; // Target reactor temperature in �C
    rTemperatureTolerance : REAL := 2.0; // Temperature tolerance in �C
    tReactionTime : TIME := T#30m; // Total reaction time
    tReactionTimer : TIME; // Reaction timer
END_VAR

// Main Sequence
IF NOT stReactionFinished THEN
    // Step 1: Load raw materials
    IF NOT stStep1 THEN
        stAmmoniaValveControl := TRUE;
        stCO2ValveControl := TRUE;
        IF stAmmoniaValve AND stCO2Valve THEN
            stStep1 := TRUE;
            tReactionTimer := CURRENT_TIME;
        END_IF
    // Step 2: Control reaction
    ELSIF NOT stStep2 THEN
        // Check pressure and temperature
        IF (rCurrentPressure >= rTargetPressure - rPressureTolerance) AND (rCurrentPressure <= rTargetPressure + rPressureTolerance) AND (rCurrentTemperature >= rTargetTemperature - rTemperatureTolerance) AND (rCurrentTemperature <= rTargetTemperature + rTemperatureTolerance) THEN
            IF CURRENT_TIME >= tReactionTimer + tReactionTime THEN
                stStep2 := TRUE;
            END_IF
        ELSE
            // Adjust valves based on pressure and temperature
            stAmmoniaValveControl := (rCurrentPressure < rTargetPressure) OR (rCurrentTemperature < rTargetTemperature);
            stCO2ValveControl := (rCurrentPressure < rTargetPressure) OR (rCurrentTemperature < rTargetTemperature);
        END_IF
    END_IF
ELSE
    stAmmoniaValveControl := FALSE;
    stCO2ValveControl := FALSE;
    stReactionFinished := TRUE;
END_IF
END_PROGRAM<br>[ChatGPT Answer](<../chatgpt/Generate Documentation Urea Reaction.md>)

### Translate ST To Instruction List:

Translate the following 61131-3 Structured Text program to 61131-3 Instruction List:
PROGRAM PickAndPlace
VAR
    ManualButton : BOOL; // Input signal for manual mode
    AutoButton : BOOL; // Input signal for auto mode
    ClipButton : BOOL; // Input signal for clip action
    TransferButton : BOOL; // Input signal for transfer action
    ReleaseButton : BOOL; // Input signal for release action
    ConveyorA : BOOL; // Input signal for presence of product on conveyor A
    ConveyorB : BOOL; // Output signal to control conveyor B
    RoboticArm : BOOL; // Output signal to control the robotic arm
    Mode : INT := 0; // Internal variable to store the current mode (0 = manual, 1 = auto)
    AutoProcess : BOOL := FALSE; // Internal variable to store whether the auto control process is currently running
END_VAR

// Manual mode control process
IF ManualButton THEN
    Mode := 0; // Set mode to manual
END_IF

IF Mode = 0 THEN // Manual mode
    IF ClipButton AND ConveyorA THEN
        RoboticArm := TRUE; // Clip the product
    ELSIF TransferButton THEN
        ConveyorB := TRUE; // Transfer the product to conveyor B
    ELSIF ReleaseButton THEN
        ConveyorB := FALSE; // Release the product from conveyor B
    END_IF
END_IF

// Auto mode control process
IF AutoButton THEN
    Mode := 1; // Set mode to auto
END_IF

IF Mode = 1 THEN // Auto mode
    IF NOT AutoProcess AND ConveyorA THEN // Only start the process if not currently running and there is a product on conveyor A
        AutoProcess := TRUE; // Set flag to indicate that the auto process is running
        RoboticArm := TRUE; // Clip the product
        WAIT 2; // Wait for 2 seconds to transfer the product
        ConveyorB := TRUE; // Transfer the product to conveyor B
    END_IF
    IF ConveyorB AND NOT ConveyorA THEN // Release the product from conveyor B once it has been transferred and there is no product on conveyor A
        ConveyorB := FALSE;
        AutoProcess := FALSE; // Clear the flag to indicate that the auto process is not running
    END_IF
END_IF<br>[ChatGPT Answer](<../chatgpt/Translate ST To Instruction List.md>)

### Optimize Batch Code:

Please make suggestions on how to optimize the following code:
PROGRAM PolyethyleneBatchControl
VAR
    // States for the batch process
    state: INT := 0;
    timer: TON;
    stepStartTime: TIME := T#0s;

    // Process parameters
    rawMatPrepTemp: REAL := 70.0; // �C
    rawMatPrepPressure: REAL := 1.0; // bar
    polymerizationTemp: REAL := 150.0; // �C
    polymerizationPressure: REAL := 30.0; // bar
    quenchingTemp: REAL := 25.0; // �C
    quenchingPressure: REAL := 5.0; // bar
    dryingTemp: REAL := 80.0; // �C
    pelletizingTemp: REAL := 150.0; // �C
    qualityControlTemp: REAL := 25.0; // �C
    packagingStorageTemp: REAL := 20.0; // �C
END_VAR

METHOD UpdateTemperaturesAndPressures: BOOL
    // Update temperatures and pressures for each process step
    CASE state OF
        1: (* Raw material preparation *)
            SetTemperatureAndPressure(rawMatPrepTemp, rawMatPrepPressure);
        2: (* Polymerization *)
            SetTemperatureAndPressure(polymerizationTemp, polymerizationPressure);
        3: (* Quenching *)
            SetTemperatureAndPressure(quenchingTemp, quenchingPressure);
        4: (* Drying *)
            SetTemperatureAndPressure(dryingTemp, quenchingPressure);
        5: (* Pelletizing *)
            SetTemperatureAndPressure(pelletizingTemp, quenchingPressure);
        6: (* Quality control *)
            SetTemperatureAndPressure(qualityControlTemp, quenchingPressure);
        7: (* Packaging and storage *)
            SetTemperatureAndPressure(packagingStorageTemp, quenchingPressure);
    END_CASE;

    RETURN TRUE;
END_METHOD

METHOD SetTemperatureAndPressure: BOOL (temp: REAL; pressure: REAL)
    // Set temperature and pressure for the current process step
    // Dummy function for demonstration purposes
    RETURN TRUE;
END_METHOD

(* Main control loop *)
LOOP
    CASE state OF
        0: (* Start the batch process *)
            state := 1;
            stepStartTime := NOW();

        1: (* Raw material preparation *)
            timer(IN:=NOT timer.Q, PT:=T#5s);
            IF timer.Q THEN
                state := 2;
                stepStartTime := NOW();
                timer(IN:=FALSE);
            END_IF;

        2: (* Polymerization *)
            timer(IN:=NOT timer.Q, PT:=T#30m);
            IF timer.Q THEN
                state := 3;
                stepStartTime := NOW();
                timer(IN:=FALSE);
            END_IF;

        3: (* Quenching *)
            timer(IN:=NOT timer.Q, PT:=T#15m);
            IF timer.Q THEN
                state := 4;
                stepStartTime := NOW();
                timer(IN:=FALSE);
            END_IF;

        4: (* Drying *)
            timer(IN:=NOT timer.Q, PT:=T#1h);
            IF timer.Q THEN
                state := 5;
                stepStartTime := NOW();
                timer(IN:=FALSE);
            END_IF;

        5: (* Pelletizing *)
            timer(IN:=NOT timer.Q, PT:=T#1h30m); 
	IF timer.Q THEN 
	state := 6;
	stepStartTime := NOW(); 
	timer(IN:=FALSE); 
	END_IF;

6: (* Quality control *)
        timer(IN:=NOT timer.Q, PT:=T#2h);
        IF timer.Q THEN
            state := 7;
            stepStartTime := NOW();
            timer(IN:=FALSE);
        END_IF;

    7: (* Packaging and storage *)
        timer(IN:=NOT timer.Q, PT:=T#3h);
        IF timer.Q THEN
            // Batch process complete
            state := 0;
            timer(IN:=FALSE);
        END_IF;

END_CASE;

UpdateTemperaturesAndPressures();

END_LOOP; 
END_PROGRAM

Consider that the program is executed cyclically in a task according to the 61131-3 programming model. Thus no explicit main loop is needed. Please fix the code by removing the 'LOOP'.<br>[ChatGPT Answer](<../chatgpt/Optimize Batch Code.md>)

### Programming Reference:

Create a list of all valid keywords in the IEC 61131-3 Structure Text programming language.<br>[ChatGPT Answer](<../chatgpt/Programming Reference.md>)

### List Mathematical Function Blocks:

Create a list of all mathematical function blocks in the OSCAT library for PLC programming.<br>[ChatGPT Answer](<../chatgpt/List Mathematical Function Blocks.md>)

### Explanation PID Function Block:

Provide a detailed explanation of the inputs and outputs of the PID function block in the OSCAT library.<br>[ChatGPT Answer](<../chatgpt/Explanation PID Function Block.md>)

### Object-oriented 61131-3:

Explain the concept of classes and methods introduced in IEC 61131-3 Version 3.0. Provide an example as well as an explanation of the limits, as well as the benefits and drawbacks of these concepts. 

How to implement inheritance in IEC 61131-3? Provide an example involving the previous code.

Refine the example to explain polymorphism in this context.<br>[ChatGPT Answer](<../chatgpt/Object-oriented 61131-3.md>)

### Learning IEC 61499:

Provide a concise introduction into the IEC 61499 programming language. Consider that I am already familiar with IEC 61131-3. Provide a list of their key differences. Create a list of five references to get more information.<br>[ChatGPT Answer](<../chatgpt/Learning IEC 61499.md>)

