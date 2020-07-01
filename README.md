
# bodyharness

## Get access to your body control module's can bus (or multiples),k-line, l-line, and other communications lines without damaging or back-probing the vehicle's electrical wiring.

This set of boards makes it possible for an external computer (via CAN) to control turn signals, lock doors, and more through the car's built-in diagnostic data connections.

Uses a two board setup, much like comma.ai car harness. Main board should stay the same for all cars and variants. The secondary board will change depending on the vehicle's requirements. This project is intended to be completely transparent to any OEM diagnostics software and also 100% reversible in minutes. No cutting any wires!

This project uses a comma.ai panda (white or grey) for the brains. The supported pandas have 3 CAN busses, K-Line, L-Line, and a single GMLAN (operates in place of one of the panda's CAN bus connections).

## Board Previews
### Main
![image info](./mainboard/main.png)
### Honda Type 1
![image info](./honda/type1/honda_type1.png)


As usual, anything on this repository is to be used AT YOUR OWN RISK! You maintain all liability.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY3MjQwOTA2MiwtMTg0Mzc5NDI1MCwtMj
E1MTMzNjExLC0xMTAyODA0NjI3LDE1MzI0MzQyOTZdfQ==
-->
