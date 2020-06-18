
# bcm_harness

## Get access to your body control module's can bus (or multiples),k-line, l-line, and other communications wiring.

This set of boards makes it possible for an external computer (via CAN) to control turn signals, lock doors, and more through the car's built-in diagnostic data connections.

Uses a two board setup, much like comma.ai car harness. Main board should stay the same for all cars and variants. The secondary board will change depending on the vehicle's requirements.

This project uses a comma.ai panda (white or grey) for the brains. The supported pandas have 3 CAN busses, K-Line, L-Line, and a single GMLAN (operates in place of one of the panda's CAN bus connections).

# Prev

![image info](./main_preview.png)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMjA1MDY2NTgsMTUzMjQzNDI5Nl19
-->