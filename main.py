#Row ends target = 2, even row = 1, odd row = 3
def getEdge(target):
  revMod = 0 if matchIdx <= 3 else 4
  edge = edgeDict[nextMatch][(matchIdx + target) % 4 + revMod]
  return edge

def addToMap(tileID, target):
  invertX, invertY = False, False
  if matchIdx > 3:
    rotations = matchIdx - target - 4
    if target in [0, 2]: 
      invertX = True
    else:
      invertY = True
  else: 
    rotations = matchIdx - target

  tile = [tileID, invertX, invertY, rotations]
  print(tile)
  if row % 2 == 0:
    tilemap[row].append(tile)
  else:
    tilemap[row].insert(0, tile)

#region Part 1
with open("tiletest") as file:
  tiles = [x.split("\n") for x in file.read().split("\n\n")]
  for i in range(len(tiles)):
    tiles[i] = [int(tiles[i][0].split(" ")[1][:-1]), tiles[i][1:]]

edgeDict = {}
matches = {}
for tile in tiles:
  left =  "".join(tile[1][i][0] for i in range(len(tile[1])))
  right = "".join(tile[1][i][-1] for i in range(len(tile[1])))
  edgeDict[tile[0]] = [tile[1][0], right, tile[1][-1], left,  tile[1][0][::-1], right[::-1], tile[1][-1][::-1], left[::-1]]
  matches[tile[0]] = []

for i in range(len(tiles)):
  for j in range(i + 1, len(tiles)):
    if set(edgeDict[tiles[i][0]]) & set(edgeDict[tiles[j][0]]):
      matches[tiles[i][0]].append(tiles[j][0])
      matches[tiles[j][0]].append(tiles[i][0])

total = 1
for tile, match in matches.items():
  if len(match) == 2:
    total *= tile
print(total)

tilemap = [[]]
for key, val in matches.items():
  if len(val) == 2:
    corner = key
    nextMatch = val[0]
row = 0
print(matches)
#endregion

#IMPORTANT: REVERSING A TILE ONLY REVERSES A SINGLE AXIS. YOU NEED TO CHECK IF BOTH AXES ARE REVERSED!

#region Part 2 First Row
  #Get the first corner to kick things off.
  #We want the corner to face the matched face east and nextMatch to face west.
f = {"North": 0, "East": 1, "South": 2, "West": 3}
edge = sorted(list(set(edgeDict[corner]) & set(edgeDict[nextMatch])))[0]
matchIdx = edgeDict[corner].index(edge)
addToMap(corner, f["East"])
matches.pop(corner)
  
matchIdx = edgeDict[nextMatch].index(edge)
addToMap(nextMatch, f["West"])
curMatch = matches.pop(nextMatch)

#Keep going til we hit a corner. 
while len(curMatch) == 3:
  edge = getEdge(2)
  for match in matches:
    if edge in edgeDict[match]:
      matchIdx = edgeDict[match].index(edge)
      addToMap(match, f["West"])
      nextMatch = match
  curMatch = matches.pop(nextMatch)

#We night need to flip. Handle flip check here. This should be the last time we need to hand check anything for a while.
edge = getEdge(3)
reverseRow = True
for match in matches:
  if edge in edgeDict[match]:
    reverseRow = False
if reverseRow:
  matchIdx += 2
  for tile in tilemap[0]:
    if tile[1] == False:
      tile[1] = True
    else:
      tile[1] = False
#endregion



  #addToMap directions: {"North": 0, "East": 1, "South": 2, "West": 3}
  #edgeDict orientation: N, E, S, W, RN, RE, RS, RW
  #Object tile: [tilenumber, reversed, rotation (1 = 90 degrees clockwise)]

while matches:
  row += 1
  tilemap.append([])
  edge = getEdge(3 if row % 2 == 1 else 1)
  for match in matches:
    if edge in edgeDict[match]:
      matchIdx = edgeDict[nextMatch].index(edge)
      addToMap(match, f["North"])
      nextMatch = match
  matches.pop(nextMatch)

  while len(tilemap[row]) < len(tilemap[0]):
    edge = getEdge(2)
    for match in matches:
      if edge in edgeDict[match]:
        matchIdx = edgeDict[nextMatch].index(edge)
        addToMap(match, f["East" if row % 2 == 1 else "West"])
        nextMatch = match
    print(tilemap)
    matches.pop(nextMatch)

  break
print(tilemap)