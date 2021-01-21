import itertools
with open("life") as file:
  cubes = [[[list(i) for i in file.read().split()]]]

def countNeighbors(cubes, w, z, y, x):
  if w == 0:
    wR = [w, w+1]
  elif w == len(cubes) - 1:
    wR = [w-1, w]
  else:
    wR = [w-1, w, w+1]

  if z == 0:
    zR = [z, z+1]
  elif z == len(cubes[0]) - 1:
    zR = [z-1, z]
  else:
    zR = [z-1, z, z+1]

  if y == 0:
    yR = [y, y+1]
  elif y == len(cubes[0][0]) - 1:
    yR = [y-1, y]
  else:
    yR = [y-1, y, y+1]  

  if x == 0:
    xR = [x, x+1]
  elif x == len(cubes[0][0][0]) - 1:
    xR = [x-1, x]
  else:
    xR = [x-1, x, x+1]

  b = list(itertools.product(wR, zR, yR, xR))
  b.remove((w, z, y, x))
  return sum(cubes[p[0]][p[1]][p[2]][p[3]] in ("#", ",") for p in b)

def printConway(cubes, generation = 0):
  print("Generation: " + str(generation))
  print("Count: " + str(sum(row.count("#") for cube in cubes for plane in cube for row in plane)))
  w = 0
  for cube in cubes:
    print("Cube #" + str(w))
    w+=1
    for plane in cube:
      for row in plane:
        print("".join(row))
      print("\n")

def printCount(cubes):
    print("Count: " + str(sum(row.count("#") for cube in cubes for plane in cube for row in plane)))

def expandCubes(cubes):
  #W-axis (new cube)
  if any('#' in row for plane in cubes[0] for row in plane):
    cubes.insert(0, [[["."] * len(cubes[0][0][0]) for row in plane] for plane in cubes[0]])
  if any('#' in y for x in cubes[-1] for y in x):
    cubes.append([[["."] * len(cubes[0][0][0]) for row in plane] for plane in cubes[0]])

  #Z-axis (new plane)
  if any('#' in row for cube in cubes for row in cube[0]):
    for cube in cubes:
      cube.insert(0, [["."] * len(cubes[0][0][0]) for row in cube[0]])
  if any('#' in row for cube in cubes for row in cube[-1]):
    for cube in cubes:
      cube.append([["."] * len(cubes[0][0][0]) for row in cube[0]])

  #Y-axis (new row)
  if any('#' in plane[0] for cube in cubes for plane in cube):
    for cube in cubes:
      for plane in cube:
        plane.insert(0, ['.'] * len(cubes[0][0][0]))
  if any('#' in plane[-1] for cube in cubes for plane in cube):
    for cube in cubes:
      for plane in cube:
        plane.append(['.'] * len(cubes[0][0][0]))

  #X-axis (new column)
  if any('#' == row[0] for cube in cubes for plane in cube for row in plane):
    for cube in cubes:
      for plane in cube:
        for row in plane:
          row.insert(0, '.')
  if any('#' == row[-1] for cube in cubes for plane in cube for row in plane):
    for cube in cubes:
      for plane in cube:
        for row in plane:
          row.append('.')


def generation(cubes):
  expandCubes(cubes)

  #Increment
  for cube in range(len(cubes)):
    for plane in range(len(cubes[0])):
      for row in range(len(cubes[0][0])):
        for x in range(len(cubes[0][0][0])):
          count = countNeighbors(cubes, cube, plane, row, x)
          if cubes[cube][plane][row][x] == "#":
            if count not in [2,3]:
              cubes[cube][plane][row][x] = ','
          else:
            if count == 3:
              cubes[cube][plane][row][x] = "*"

  for cube in range(len(cubes)):
    for plane in range(len(cubes[0])):
      for row in range(len(cubes[0][0])):
        for x in range(len(cubes[0][0][0])):
          if cubes[cube][plane][row][x] == ",":
            cubes[cube][plane][row][x] = "."
          elif cubes[cube][plane][row][x] == "*":
            cubes[cube][plane][row][x] = "#"

gen = 1
while gen <= 6: