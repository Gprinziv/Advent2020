def getOppEdge():
  opposite = {0:2, 1:3, 2:0, 3:1, 4:6, 5:7, 6:4, 7:5}
  return edgeDict[nextMatch][opposite[edgeIdx]]

def getCorner(target = None):
  east = {0:1, 1:6, 2:5, 3:2, 4:3, 5:4, 6:7, 7:0} #also westsouth, apparently
  west = {0:3, 1:4, 2:7, 3:0, 4:1, 5:6, 6:5, 7:2}
  eastsouth = {0:5, 1:2, 2:1, 3:6, 4:7, 5:0, 6:3, 7:4}

  if target == "east":
    return edgeDict[nextMatch][east[edgeIdx]]
  elif target == "west":
    return edgeDict[nextMatch][west[edgeIdx]]
  else:
    if row % 2 == 0:
      return edgeDict[nextMatch][east[edgeIdx]]
    else:
      return edgeDict[nextMatch][eastsouth[edgeIdx]]

def addToMap(tileID, target):
  if row % 2 == 0:
    tilemap[row].append([tileID, edgeIdx, target])
  else:
    tilemap[row].insert(0, [tileID, edgeIdx, target])

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

tilemap = [[]]
for key, val in matches.items():
  if len(val) == 2:
    corner = key
    nextMatch = val[0]
#endregion
#region Part 1 output
#print(total)
#print(matches)
#endregion

#region Part 2 Generate tile map.
#First, we need to find the two matching edges from wahtever we decided was the corner.
row = 0
edge = sorted(list(set(edgeDict[corner]) & set(edgeDict[nextMatch])))[0]
edgeIdx = edgeDict[corner].index(edge)
addToMap(corner, "east")
matches.pop(corner)

edgeIdx = edgeDict[nextMatch].index(edge)
addToMap(nextMatch, "west")
curMatch = matches.pop(nextMatch)

#Keep going til we hit a corner. 
while len(curMatch) == 3:
  edge = getOppEdge()
  for tile in matches:
    if edge in edgeDict[tile]:
      edgeIdx = edgeDict[tile].index(edge)
      addToMap(tile, "west")
      nextMatch = tile
  curMatch = matches.pop(nextMatch)

#potentially invert the first row
edge = getCorner()
reverse = True
for tile in matches:
  if edge in edgeDict[tile]:
    reverse = False
if reverse:
  for tile in tilemap[0]:
    tile[1] = (tile[1] + 4) % 8
  edgeIdx = (edgeIdx + 4) % 8

#Complete the map
while matches:
  tilemap.append([])
  edge = getCorner()
  row += 1
  for tile in matches:
    if edge in edgeDict[tile]:
      edgeIdx = edgeDict[tile].index(edge)
      addToMap(tile, "north")
      nextMatch = tile
  matches.pop(nextMatch)

  edge = getCorner("west" if row % 2 == 1 else "east")
  while len(tilemap[row]) < len(tilemap[0]):
    for tile in matches:
      if edge in edgeDict[tile]:
        edgeIdx = edgeDict[tile].index(edge)
        addToMap(tile, "east" if row % 2 == 1 else "west")
        nextMatch = tile
    matches.pop(nextMatch)
    edge = getOppEdge()
#endregion
print(tilemap)
#region Create initial string array
  #For each tile in a tilerow, figure out how many rotations it would take to face the given direction, and which axes would need to be reversed.
  #Then, using that schema, create a 2d string array, removing the outer border.
  #For each additional tile in the same tilerow, add to the end of each existing string.
  #When you go to a new tilerow, append rows to the string array.
#endregion
#region search for nessie

#endregion
#region rotate and repeat x3

#endregion