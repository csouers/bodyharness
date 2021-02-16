# Fake the Honda headunit's navigation data to CAN interface

# from selfdrive.car.honda.bodyvalues import DBC
from checksum import honda_body_checksum

class CurrentStreet():
  # index #
  # 01: 0e + padding
  # 02 - 06: nth chunk
  
  def __init__(self):
    self.index = 2
    self.d1 = 0
    self.d2 = 0
    self.d3 = 0
    self.d4 = 0
    self.d5 = 0
    self.d6 = 0
    self.checksum = 0
  def pack(self, string):
    l = len(string)
    i = l / 6
    return i

class CarNav():
  def __init__(self):
    #current street
    self.currentStreetIdx = 0  # 1-4
    self.currentStreet = ''
    self.currentStreetLast = ''


  def update(self):
    pass


def main():
  # dat = 0x037369666572200e
  # len = 8
  #
  # sum = honda_body_checksum(dat, len)
  # print(sum)

  c = CurrentStreet()
  c_pack = c.pack('stansifer')
  print(c_pack)

if __name__ == '__main__':
  main()
