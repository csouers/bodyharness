# This script was supposed to reveal if we could control the navigation screen in the meter (instrument panel)
# However, nothing I sent had any affect. The hardware uses a high speed coaxial display connection from the headunit to the meter.
# Does the meter really use the CAN data for this? Or is it just an intermediary to be read back into the headunit and then
# pipe the data over the display connection?

# Some ideas on why it didn't work if the former is true:
# - I didn't send the full next turn packet on 0x12f95954
# - I didn't send the other multi-frame packet on 0x12f95c54 (I don't yet know what this frame is used for)

from panda import Panda
import time
p = Panda()
# not needed if your panda firmware defaults to an appropriate safety model
# p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
MIN_BYTE = 0x5f
MAX_BYTE = 0xff

for x in range(MIN_BYTE, MAX_BYTE+1):
    print(hex(x))
    # make the data string
    # # TODO: this is ugly
    dat = bytes([0x00])
    dat += bytes([0x45])
    dat += bytes([0x0f])
    dat += bytes([0x00])
    dat += bytes([0x83])
    dat += bytes([x])
    dat += bytes([0x40])
    dat += bytes([0x03])
    p.can_send(0x12f95954, dat, 1)

    dat2 = bytes([0x01])
    dat2 += bytes([0x02])
    dat2 += bytes([0x80])
    dat2 += bytes([0x00])
    dat2 += bytes([0x00])
    dat2 += bytes([0x00])
    dat2 += bytes([0x00])
    dat2 += bytes([0x0b])
    p.can_send(0x12f95c54, dat2, 1)

    dat3 = bytes([0x10])
    dat3 += bytes([0x0e])
    dat3 += bytes([0x00])
    dat3 += bytes([0x00])
    dat3 += bytes([0x00])
    dat3 += bytes([0x00])
    dat3 += bytes([0x00])
    dat3 += bytes([0x0f])
    p.can_send(0x12f95e54, dat3, 1)

    dat4 = bytes([0x20])
    dat4 += bytes([0x00])
    dat4 += bytes([0x15])
    dat4 += bytes([0x03])
    p.can_send(0x12f95b54, dat4, 1)

    dat5 = bytes([0x20])
    dat5 += bytes([0x00])
    dat5 += bytes([0x1c])
    dat5 += bytes([0x04])
    p.can_send(0x12f95d54, dat5, 1)

    time.sleep(0.25)
    # input("Next?")
