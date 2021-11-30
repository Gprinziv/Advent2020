def getOppEdge():
  opposite = {0:2, 1:3, 2:0, 3:1, 4:6, 5:7, 6:4, 7:5}
  return edgeDict[nextMatch][opposite[edgeIdx]]

def getCorner(target):
  north = {0:1, 1:4, 2:7, 3:0, 4:3, 5:6, 6:5, 7:2}
  south = {0:1, 1:6, 2:5, 3:2, 4:3, 5:4, 6:7, 7:0}
  if target == 1:
    return edgeDict[nextMatch][north[edgeIdx]]
  else:
    return edgeDict[nextMatch][south[edgeIdx]]

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

tilemap = [[]]
for key, val in matches.items():
  if len(val) == 2:
    corner = key
    nextMatch = val[0]
#endregion
#region Part 1 output
#print(total)
print(matches)
#endregion

#region Part 2 First Row
#First, we need to find the two matching edges from wahtever we decided was the corner.
row = 0
edge = sorted(list(set(edgeDict[corner]) & set(edgeDict[nextMatch])))[0]
edgeIdx = edgeDict[corner].index(edge)
addToMap(corner, "East")
matches.pop(corner)

edgeIdx = edgeDict[nextMatch].index(edge)
addToMap(nextMatch, "West")
curMatch = matches.pop(nextMatch)

#Keep going til we hit a corner. 
while len(curMatch) == 3:
  edge = getOppEdge()
  for tile in matches:
    if edge in edgeDict[tile]:
      edgeIdx = edgeDict[tile].index(edge)
      addToMap(tile, "West")
      nextMatch = tile
  curMatch = matches.pop(nextMatch)
#endregion
#region Part 2 First Corner
#Check South first. If you can't find it, reverse the entire tileset.
edge = getCorner(-1)
reverse = True
for tile in matches:
  if edge in edgeDict[tile]:
    reverse = False
if reverse:
  for tile in tilemap[0]:
    tile[1] = (tile[1] + 4) % 8
  edgeIdx = (edgeIdx + 4) % 8
#endregion
#region Part 2 Loop to the end
while matches:
  row += 1
  print("Row " + str(row))
  tilemap.append([])
  print(tilemap)
  edge = getCorner(-1 if row % 2 == 1 else 1)
  for tile in matches:
    if edge in edgeDict[tile]:
      edgeIdx = edgeDict[tile].index(edge)
      addToMap(tile, "North")
      nextMatch = tile
  matches.pop(nextMatch)
  print(tilemap)
  edge = getCorner(-1 if row % 2 == 1 else 1)
  while len(tilemap[row]) < len(tilemap[0]):
    for tile in matches:
      if edge in edgeDict[tile]:
        edgeIdx = edgeDict[tile].index(edge)
        addToMap(tile, "East" if row % 2 == 1 else "West")
        nextMatch = tile
    matches.pop(nextMatch)
    edge = getOppEdge()
#Reverse east should point to north. What did I do?


#endregion
print(tilemap)