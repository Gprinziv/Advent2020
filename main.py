from os import name
def part1():
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

  return edgeDict, matches

#Row ends target = 2, even row = 1, odd row = 3
def getEdge(edgeList, matchIdx, target):
  revMod = 0 if matchIdx <= 3 else 4
  edge = edgeList[(matchIdx + target) % 4 + revMod]
  return edge

def addToMap(nextMatch, matchIdx, target, tilemap, row):
  f = {"East": 1, "South": 2, "West": 3}
  invert = False
  print(matchIdx)
  if matchIdx > 3:
    print("inverting.")
    rotations = matchIdx - f[target] - 4
    invert = True
  else: 
    rotations = matchIdx - f[target]

  tile = [nextMatch, invert, rotations]
  print(tile)
  if row % 2 == 0:
    tilemap[row].append(tile)
  else:
    tilemap[row].insert(0, tile)

#Get the first corner to kick things off.
def part2(edgeDict, matches):
  tilemap = [[]]
  for key, val in matches.items():
    if len(val) == 2:
      corner = key
      nextMatch = val[0]
  row = 0

  #We want next (corner) to face the matched face east and nextMatch to face west.
  edge = sorted(list(set(edgeDict[corner]) & set(edgeDict[nextMatch])))[0]
  matchIdx = edgeDict[corner].index(edge)
  addToMap(corner, matchIdx, "East", tilemap, row)
  matches.pop(corner)
  
  matchIdx = edgeDict[nextMatch].index(edge)
  addToMap(nextMatch, matchIdx, "West", tilemap, row)
  curMatch = matches.pop(nextMatch)

  #Keep going til we hit a corner. 
  while len(curMatch) == 3:
    edge = getEdge(edgeDict[nextMatch], matchIdx, 2)
    for match in matches:
      if edge in edgeDict[match]:
        matchIdx = edgeDict[nextMatch].index(edge)
        addToMap(match, matchIdx, "West", tilemap, row)
        nextMatch = match
    curMatch = matches.pop(nextMatch)

  #We night need to flip. Handle flip check here. This should be the last time we need to hand check anything for a while.
  revMod = 0 if matchIdx <= 3 else 4
  edge = edgeDict[nextMatch][(matchIdx + 3) % 4 + revMod]
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

  #edgeDict orientation: N, E, S, W, RN, RE, RS, RW
  #Object tile: [tilenumber, reversed, rotation (1 = 90 degrees clockwise)]

  while matches:
    row += 1
    tilemap.append([])
    edge = getEdge(edgeDict[nextMatch], matchIdx, 3 if row % 2 == 1 else 1)
    for match in matches:
      if edge in edgeDict[match]:
        matchIdx = edgeDict[nextMatch].index(edge)
        addToMap(match, matchIdx, "South", tilemap, row)
        nextMatch = match
    matches.pop(nextMatch)

    while len(tilemap[row]) < len(tilemap[0]):    
      revMod = 0 if matchIdx <= 3 else 4
      edge = getEdge(edgeDict[nextMatch], matchIdx, 2)
      for match in matches:
        if edge in edgeDict[match]:
          matchIdx = edgeDict[nextMatch].index(edge)
          addToMap(match, matchIdx, ("East" if row % 2 == 1 else "West"), tilemap, row)
          nextMatch = match
      print(tilemap)
      matches.pop(nextMatch)

    #Now that we know how long a "row" is, let's automate.
    #Increment the row, append an empty list to it.
    #The first time should always be looking "down".
      #If the row is even, that means looking for a edge at the prior matchIdx + 3
      #If the row is odd, that means looking for a edge at the prior index + 1
    #Add the tile.
    #Determine if you're going east or west.
    #Continue until you get to the end of the row
    #repeat until you're out of tiles.

    break
  
  print(tilemap)

edgeDict, matches = part1()
part2(edgeDict, matches)