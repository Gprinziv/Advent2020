with open("movement") as file:
  moves = [i.strip() for i in file]

class Ship:
  dirs = {0: "E", 90: "S", 180: "W", 270: "N"}
  coords = {"N": 0, "E": 0, "W": 0, "S": 0}
  heading = 0

  def move(self, direction, distance):
    if direction == "F":
      direction = self.dirs[self.heading]
    self.coords[direction] += distance

  def setHeading(self, rotation):
    self.heading = (self.heading + rotation) % 360

  def getManhattan(self):
    coords = self.getPosition()
    return abs(coords[0]) + abs(coords[1])

  def getPosition(self):
    return [
      self.coords["E"] - self.coords["W"], 
      self.coords["S"] - self.coords["N"]
      ]

  def __init__(self):
    pass

class WayShip():
  x, y, wayX, wayY = 0, 0, 10, -1

  def move(self, times):
    
    self.x += self.wayX * times
    self.y += self.wayY * times

  def moveWaypoint(self, direction, value):
    if direction == "N":
      self.wayY -= value
    elif direction == "E":
      self.wayX += value
    elif direction == "W":
      self.wayX -= value
    else:
      self.wayY += value

  def setHeading(self, rotation):
    rotation = (rotation % 360)
    if rotation == 90:
      self.wayX, self.wayY = -self.wayY, self.wayX
    elif rotation == 180:
      self.wayX, self.wayY = -self.wayX, -self.wayY
    elif rotation == 270:
      self.wayX, self.wayY = self.wayY, -self.wayX

  def getPosition(self):
    return [self.x, self.y]

  def getWaypoint(self):
    return [self.wayX, self.wayY]

  def getManhattan(self):
    return abs(self.x) + abs(self.y)

  def __init__(self):
    pass

#Part 1
ferry = Ship()
for move in moves:
  inst = move[0]
  val = int(move[1:])

  if inst == "L":
    ferry.setHeading(-val)
  elif inst == "R":
    ferry.setHeading(val)
  else:
    ferry.move(inst, val)
print(ferry.getManhattan())

#Part 2
ferry = WayShip()
for move in moves:
  inst = move[0]
  val = int(move[1:])
  if inst == "L":
    ferry.setHeading(-val)
  elif inst == "R":
    ferry.setHeading(val)
  elif inst == "F":
    ferry.move(val)
  else:
    ferry.moveWaypoint(inst, val)
print(ferry.getManhattan())