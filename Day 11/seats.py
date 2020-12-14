with open("ferry") as file:
  seats = [i.strip() for i in file]

seatAdjacency = {}
adjacentFilled= {}
for y in range(len(seats)):
  for x in range(len(seats[0])):
    if seats[y][x] == "L":
      seatAdjacency[(x, y)] = []
      adjacentFilled[(x, y)] = 0
"""
#Part 1
for seat in seatAdjacency:
  for x in range(seat[0] - 1, seat[0] + 2):
    for y in range(seat[1] - 1, seat[1] + 2):
      if (x, y) in seatAdjacency and seat != (x, y):
        seatAdjacency[seat].append((x, y))
"""
#Part 2
for seat in seatAdjacency:
  for x in range(seat[0] - 1, -1, -1):
    if seats[seat[1]][x] == "L":
        seatAdjacency[seat].append((x, seat[1]))
        break
  for x in range(seat[0] + 1, len(seats[0])):
    if seats[seat[1]][x] == "L":
        seatAdjacency[seat].append((x, seat[1]))
        break
  for y in range(seat[1] - 1, -1, -1):
    if seats[y][seat[0]] == "L":
        seatAdjacency[seat].append((seat[0], y))
        break
  for y in range(seat[1] + 1, len(seats)):
    if seats[y][seat[0]] == "L":
        seatAdjacency[seat].append((seat[0], y))
        break
  for x, y in zip(range(seat[0] - 1, -1, -1), range(seat[1] - 1, -1, -1)):
    if seats[y][x] == "L":
      seatAdjacency[seat].append((x, y))
      break
  for x, y in zip(range(seat[0] + 1, len(seats[0])), range(seat[1] - 1, -1, -1)):
    if seats[y][x] == "L":
      seatAdjacency[seat].append((x, y))
      break
  for x, y in zip(range(seat[0] - 1, -1, -1), range(seat[1] + 1, len(seats))):
    if seats[y][x] == "L":
      seatAdjacency[seat].append((x, y))
      break
  for x, y in zip(range(seat[0] + 1, len(seats[0])), range(seat[1] + 1, len(seats))):
    if seats[y][x] == "L":
      seatAdjacency[seat].append((x, y))
      break

changed = True
while(changed == True):
  changed = False

  #4 for Part 1, 5 for Part 2
  for seat in seatAdjacency:
    if adjacentFilled[seat] == 0 and seats[seat[1]][seat[0]] == "L":
      seats[seat[1]] = seats[seat[1]][:seat[0]] + "#" + seats[seat[1]][seat[0] + 1:]
      changed = True
    elif adjacentFilled[seat] >= 5 and seats[seat[1]][seat[0]] == "#":
      seats[seat[1]] = seats[seat[1]][:seat[0]] + "L" + seats[seat[1]][seat[0] + 1:]
      changed = True

  for seat in seatAdjacency:
    adjacentFilled[seat] = 0
    for adjacent in seatAdjacency[seat]:
      if seats[adjacent[1]][adjacent[0]] == "#":
        adjacentFilled[seat] += 1

print(sum(i.count("#") for i in seats))