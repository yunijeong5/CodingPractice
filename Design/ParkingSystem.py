class ParkingSystem:
  def __init__(self, big: int, medium: int, small: int):
    self.slots = [0, big, medium, small]

  def addCar(self, carType: int) -> bool:
    if type(carType) != int or carType > 3 or carType < 1:
      exit("invalid car type")

    if self.slots[carType] > 0:
      self.slots[carType] -= 1
      return True
    else:
      return False

# Time: O(1), Space: O(1)