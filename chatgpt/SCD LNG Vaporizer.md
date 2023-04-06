Model: GPT-4

> Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

A NORSOK System Control Diagram (SCD) for a Liquefied Natural Gas (LNG) Vaporizer System in textual notation is as follows:

1.  LNG Inlet Line:

*   Piping: P100
*   Inlet Valve: IV-101 (interlocked with FIC-104)
*   Flow Transmitter: FT-101
*   Pressure Transmitter: PT-101
*   Temperature Transmitter: TT-101

2.  LNG Vaporizer:

*   Piping: P200
*   Vaporizer Unit: VAP-201
*   Inlet Valve: IV-202 (interlocked with FIC-203)
*   Outlet Valve: OV-203
*   Pressure Control Valve: PCV-204 (controlled by PIC-205)
*   Temperature Control Valve: TCV-206 (controlled by TIC-207)
*   Pressure Transmitter: PT-202
*   Temperature Transmitter: TT-202
*   Flow Transmitter: FT-202
*   Pressure Indicator Controller: PIC-205
*   Temperature Indicator Controller: TIC-207
*   Flow Indicator Controller: FIC-203 (Cascade control with FIC-104)

3.  Natural Gas Outlet Line:

*   Piping: P300
*   Outlet Valve: OV-301
*   Flow Transmitter: FT-301
*   Pressure Transmitter: PT-301
*   Temperature Transmitter: TT-301

4.  Control Loops and Instrumentation:

*   Flow control loop: FIC-104 controls IV-101 based on the flow setpoint and feedback from FT-101.
*   Pressure control loop: PIC-205 controls PCV-204 based on the pressure setpoint and feedback from PT-202.
*   Temperature control loop: TIC-207 controls TCV-206 based on the temperature setpoint and feedback from TT-202.

5.  Interlocks:

*   IV-101 is interlocked with FIC-104, such that the valve closes if the flow rate exceeds the high flow limit.
*   IV-202 is interlocked with FIC-203, such that the valve closes if the flow rate in the vaporizer exceeds the high flow limit.

The LNG flows through the inlet line (P100), with the flow rate controlled by IV-101 and monitored by FT-101. The pressure and temperature of the inlet LNG are monitored by PT-101 and TT-101, respectively. The LNG then enters the vaporizer (VAP-201) through IV-202, where it is heated and vaporized. The vaporization process is controlled by adjusting the pressure using PCV-204 and temperature using TCV-206. The pressure and temperature of the vaporized gas are monitored by PT-202 and TT-202. The vaporized natural gas flows through the outlet line (P300) and is monitored by FT-301, PT-301, and TT-301.