def getOppEdge():
  revMod = 0 if matchIdx <= 3 else 4
  edge = edgeDict[nextMatch][(matchIdx + 2) % 4 + revMod]
  return edge

def getCornerEdge(target):
  pass

def addToMap(tileID, target):
  flipX, flipY = False, False
  if matchIdx > 3:
    rotations = matchIdx - target - 4
    if target == 0:
      flipX = True
    else:
      flipY = True
  else: 
    rotations = matchIdx - target

  tile = [tileID, flipY, flipX, rotations]

  if row % 2 == 0:
    tilemap[row].append(tile)
  else:
    tilemap[row].insert(0, tile)
  return tile

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
  edgeDict[tile[0]] = [tile[1][0], right, tile[1][-1], left,  tile[1][0], right[::-1], tile[1][-1][::-1], left[::-1]]
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

#region Part 2 First Tiles
#First, we need to find the two matching edges from wahtever we decided was the corner.
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
  edge = getOppEdge()
  for match in matches:
    if edge in edgeDict[match]:
      matchIdx = edgeDict[match].index(edge)
      addToMap(match, f["West"])
      nextMatch = match
  curMatch = matches.pop(nextMatch)

edge = getCornerEdge(f["South"]) #Write this code

#If the corner isn't reversed, 


print(edge)
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


  #edgeDict orientation: N, E, S, W, RN, RE, RS, RW
  #Object tile: [tilenumber, reversed, rotation (1 = 90 degrees clockwise)]

#revisit this later. It's not ready until I can create a stable map for the fudging tiles.
while matches:
  row += 1
  tilemap.append([])
  edge = getEdge(-1 if row % 2 == 1 else 1)
  print(edge)
  for match in matches:
    if edge in edgeDict[match]:
      matchIdx = edgeDict[nextMatch].index(edge)
      addToMap(match, f["North"])
      nextMatch = match
  matches.pop(nextMatch)
  edge = getEdge(-1 if row % 2 == 1 else 1)
  print(edge)
  print(edgeDict[nextMatch].index(edge))
  print(edgeDict[nextMatch])

  while len(tilemap[row]) < len(tilemap[0]):
    for match in matches:
      if edge in edgeDict[match]:
        matchIdx = edgeDict[nextMatch].index(edge)
        addToMap(match, f["East" if row % 2 == 1 else "West"])
        nextMatch = match
    print(tilemap)
    matches.pop(nextMatch)
    edge = getOppEdge()

  break
print(tilemap)