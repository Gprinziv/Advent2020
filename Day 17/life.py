import itertools
with open("life") as file:
  cubes = [[list(i) for i in file.read().split()]]

def countNeighbors(cubes, z, y, x):
  if z == 0:
    zR = [z, z+1]
  elif z == len(cubes) - 1:
    zR = [z-1, z]
  else:
    zR = [z-1, z, z+1]

  if y == 0:
    yR = [y, y+1]
  elif y == len(cubes[0]) - 1:
    yR = [y-1, y]
  else:
    yR = [y-1, y, y+1]  

  if x == 0:
    xR = [x, x+1]
  elif x == len(cubes[0][0]) - 1:
    xR = [x-1, x]
  else:
    xR = [x-1, x, x+1]

  b = list(itertools.product(zR, yR, xR))
  b.remove((z, y, x))
  return sum(cubes[p[0]][p[1]][p[2]] in ("#", ",") for p in b)

def printConway(cubes, generation = 0):
  print("Generation: " + str(generation))
  print("Count: " + str(sum(row.count("#") for plane in cubes for row in plane)))
  for cube in cubes:
    for row in cube:
      print("".join(row))
    print("\n")

def generation(cubes):
  #Z-axis
  if any('#' in x for x in cubes[0]):
    cubes.insert(0, [['.'] * len(cubes[0][0]) for i in cubes[0]])
  if any('#' in x for x in cubes[len(cubes) - 1]):
    cubes.append([['.'] * len(cubes[0][0]) for i in cubes[0]])

  #Y-axis
  if any('#' in cubes[z][0] for z in range(len(cubes))):
    for i in range(len(cubes)):
      cubes[i].insert(0, ['.'] * len(cubes[0][0]))
  if any('#' in cubes[z][len(cubes[0]) - 1] for z in range(len(cubes))):
      for i in range(len(cubes)):
        cubes[i].append(['.'] * len(cubes[0][0]))

  #X-axis
  if (any('#' in cubes[z][y][0]) for z in cubes for y in cubes[z]):
    for plane in cubes:
      for row in plane:
        row.insert(0, '.')
  if (any('#' in cubes[z][y][len(cubes[0][0]) - 1]) for z in cubes for y in cubes[z]):
    for plane in cubes:
      for row in plane:
        row.append('.')

  #Increment
  for z in range(len(cubes)):
    for y in range(len(cubes[z])):
      for x in range(len(cubes[z][y])):
        count = countNeighbors(cubes, z, y, x)
        if cubes[z][y][x] == "#":
          if count not in [2, 3]:
            cubes[z][y][x] = ","
        else:
          if count == 3:
            cubes[z][y][x] = "*"

  for z in range(len(cubes)):
    for y in range(len(cubes[z])):
      for x in range(len(cubes[z][y])):
        if cubes[z][y][x] == ",":
          cubes[z][y][x] = "."
        elif cubes[z][y][x] == "*":
          cubes[z][y][x] = "#"

printConway(cubes)
gen = 1
while gen <= 6:
  generation(cubes)
  printConway(cubes, gen)
  gen += 1