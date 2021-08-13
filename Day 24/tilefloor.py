with open("fliptiles") as file:
  tiles = file.read().split("\n")

minx, maxx, miny, maxy = 0, 0, 0, 0
for tile in tiles:
  ptr, curx, cury = 0, 0, 0 
  while ptr < len(tile):
    if tile[ptr] == "e":
      curx += 1
      ptr += 1
    elif tile[ptr] == "w":
      curx -= 1
      ptr +=1 
    elif tile[ptr] == "n":
      if tile[ptr + 1] == "e":
        if cury % 2 == 1:
          curx += 1
      else:
        if cury % 2 == 0:
          curx -= 1
      cury -= 1
      ptr += 2
    else:
      if tile[ptr + 1] == "e":
        if cury % 2 == 1:
          curx += 1
      else:
        if cury % 2 == 0:
          curx -= 1
      cury += 1
      ptr += 2

    if curx < minx:
      minx = curx
    if curx > maxx:
      maxx = curx
    if cury < miny:
      miny = cury
    if cury > maxy:
      maxy = cury

rel = (-minx, -miny)
tilemap = [[0] * (maxx + 1 - minx) for i in range(maxy + 1 - miny)]

for tile in tiles:
  ptr, curx, cury = 0, rel[0], rel[1]
  while ptr < len(tile):
    if tile[ptr] == "e":
      curx += 1
      ptr += 1
    elif tile[ptr] == "w":
      curx -= 1
      ptr +=1 
    elif tile[ptr] == "n":
      if tile[ptr + 1] == "e":
        if cury % 2 == 1:
          curx += 1
      else:
        if cury % 2 == 0:
          curx -= 1
      cury -= 1
      ptr += 2
    else:
      if tile[ptr + 1] == "e":
        if cury % 2 == 1:
          curx += 1
      else:
        if cury % 2 == 0:
          curx -= 1
      cury += 1
      ptr += 2

  tilemap[cury][curx] += 1

total = 0
with open("teststart", "w") as file:
  for tilerow in tilemap:
    file.write(" ".join("{:2d}".format(tile) for tile in tilerow))
    file.write("\n")
    for tile in tilerow:
      if tile % 2 == 1:
        total += 1
print(total)