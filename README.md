
# bodyharness (Work in Progress)

## Expand your openpilot experience with access to your vehicle's chassis CAN bus

Available for purchase at https://autofocuser.com!

This hardware, together with the necessary software, makes it possible to electronically control turn signals, door locks, and more. Future software will support features such as low fuel warnings, unlocked vehicle notifications, and headlights on during comma prime snapshots.

Currently, a comma.ai panda (white or grey) is the only required accessory. The black panda can be supported with additional effort (no plans for this at the moment). The supported pandas have 3 CAN bus transceivers, k-line and l-line connections, and a single GMLAN connection (operates in place of one of the panda's CAN bus connections). Future hardware revisions will support LIN (k-line and l-line).

## Compatibility
##### Based on vehicle generation. Vehicles may vary. Check your car first!
| Make | Model | B-CAN Connection Location |
| -- | -- | -- |
| Acura     | ILX 2016-18                   | TBD                                                                                             |
| Acura     | RDX 2016-18                   | TBD                                                                                           |
| Honda     | Accord 2018-20                | Option Connector (Pinout A) PINK 2+ / BLUE 3-                                                |
| Honda     | Accord Hybrid 2018-20         | Option Connector (Pinout A) PINK 2+ / BLUE 3-                                                |
| Honda     | Civic Hatchback 2017-19       | Option Connector (Pinout A) PINK 2+ / BLUE 3-                                                |
| Honda     | Civic Sedan/Coupe 2016-18     | Option Connector (Pinout A) PINK 2+ / BLUE 3-                                                |
| Honda     | Civic Sedan/Coupe 2019-20     | Option Connector (Pinout A) PINK 2+ / BLUE 3-                                                |                                              
| Honda     | CR-V 2015-16                  | (DIY) at BCM/Under Dash Fuse Box or other module                                             |
| Honda     | CR-V 2017-20                  | Option Connector (Pinout A) PINK 2+ / BLUE 3-                                                |                                              
| Honda     | CR-V Hybrid 2017-2019         | Option Connector (Pinout A) PINK 2+ / BLUE 3-                                                |
| Honda     | Fit 2018-19                   | (DIY) 2018 at BCM/Under Dash Fuse/Relay Box or other module - 2019+ at ADAS Camera Connector |
| Honda     | HR-V 2019-2021                | (DIY) at ADAS Camera Connector                                                               |
| Honda     | Insight 2019-20               | (DIY) at BCM/Under Dash Fuse/Relay Box or other module                                       |
| Honda     | Odyssey 2018-20               | Option Connector (Pinout B) PINK 2+ / BLUE 5-                                                |
| Honda     | Passport 2019                 | (DIY) BCM/Under Dash Fuse/Relay Box or other module - 2020+ at ADAS Camera Connector         |
| Honda     | Pilot 2016-19                 | (DIY) BCM/Under Dash Fuse/Relay or other module - 2019+ at ADAS Camera Connector             |
| Honda     | Ridgeline 2017-20             | (DIY) BCM/Under Dash Fuse/Relay or other module - 2020+ at ADAS Camera Connector             |

As usual, anything on this repository is to be used AT YOUR OWN RISK! You maintain all liability.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAyMDg2MzIxNCw4MjI2NDQ3OTEsLTk1Nj
MwMjA3NiwtMTA4NjM2NzEwMiwxNDYwOTY0NjcxLDE2NzI0MDkw
NjIsLTE4NDM3OTQyNTAsLTIxNTEzMzYxMSwtMTEwMjgwNDYyNy
wxNTMyNDM0Mjk2XX0=
-->
