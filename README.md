
# bodyharness (Work in Progress)

## Get access to your body control module's can bus (or multiples), k-line, l-line, and other communication lines without damaging or back-probing the vehicle's electrical wiring.

This set of boards, together with the necessary sofware, makes it possible for an external computer to control turn signals, windows, doors, and more.

Uses a two board setup, much like comma.ai car harness. In final form, the main board will stay the same for all cars and variants. The secondary board will change depending on the vehicle's requirements. This project is intended to be completely transparent to any OEM diagnostics software and also 100% reversible in minutes. No cutting any wires!

This project uses a comma.ai panda (white or grey) for the brains. The supported pandas have 3 CAN busses, K-Line, L-Line, and a single GMLAN (operates in place of one of the panda's CAN bus connections).

## Board Previews
### Main
![image info](./mainboard/main.png)
### Honda Type 1
#### Compatible:
Honda Civic Hatchback 2017 (US Market)<br>
Honda CR-V 2017 (US Market)<br>
#### Incompatible
Honda Accord 2018+ (US Market)<br>
![image info](./honda/type1/honda_type1.png)


As usual, anything on this repository is to be used AT YOUR OWN RISK! You maintain all liability.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwODYzNjcxMDIsMTQ2MDk2NDY3MSwxNj
cyNDA5MDYyLC0xODQzNzk0MjUwLC0yMTUxMzM2MTEsLTExMDI4
MDQ2MjcsMTUzMjQzNDI5Nl19
-->