from panda import Panda
import time
p = Panda()
#p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
MIN_BYTE = 0x00
MAX_BYTE = 0xff


for x in range(MIN_BYTE, MAX_BYTE+1):
    print(hex(x))
    # make the data string
    dat = bytes([0x30])
    dat += bytes([x])
    dat += bytes([0x0f])
    dat += bytes([0x0])
    dat += bytes([0x0])
    dat += bytes([0x0])
    dat += bytes([0x0])
    dat += bytes([0x0])

    # send it
    p.can_send(0x16F118F0, dat , 1)
    time.sleep(1)
    # stop
    p.can_send(0x16F118F0, b'\x20', 1)
    time.sleep(0.1)
    input("Next?")
