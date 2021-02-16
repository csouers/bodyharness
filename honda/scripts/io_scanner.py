from panda import Panda
import time

BCM = 0x16F118F0


def main():
  p = Panda()
  # p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)   # Set this if panda safety doesn't allow you to send to the desired module.
  MIN_BYTE = 0x00
  MAX_BYTE = 0xff
  MODULE_ID = BCM
  CANCEL_CMD = b'\x20'

  print("Connected to panda. Press enter to step through each command.")
  print("Use Control-C to exit.")

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
      p.can_send(MODULE_ID, dat, 1)
      time.sleep(2)

      # send the all test cancel
      p.can_send(MODULE_ID, CANCEL_CMD, 1)
      time.sleep(0.1)
      input("Next?")



if __name__ == '__main__':
  main()
