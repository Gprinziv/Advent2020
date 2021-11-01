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
      #print(tile)
      total *= tile
  print(total)

  return edgeDict, matches

#Choose one of the tiles that only has two matches and designate it (0, 0). Choose one of the matches and designate it (0,1).
#Find the side of (0,1) that matches the (0,0), orient it, and repeat, finsing the side of (0,2). Repeat until you get to the "corner".
#Then find the other match for the corner, (1, n), and work backwards to (1,0). Then (2, 0) to (2, n) and repeat. I could clean out the "matches" map as I go to save time.



#Get the first corner to kick things off.
def part2(edgeDict, matches):
  facings = {0:(), 1:(), 2:(), 3:() ,4:() ,5:() , 6:(), 7:()}
  target = 0

  tilemap = [[]]
  for key, val in matches.items():
    if len(val) == 2:
      next = key
      nextMatch = val[0]

  #We want next (corner) to face the matched face east and nextMatch to face west.
  matchEdge = sorted(list(set(edgeDict[next]) & set(edgeDict[nextMatch])))[0]
  
  #edgeDict orientation: N, E, S, W, RN, RE, RS, RW
  rotations = edgeDict[next].index(matchEdge) - 1
  print("Rotations: " + str(rotations)) #This seems right. Need to check for reversedness, too.
  rotations = edgeDict[nextMatch].index(matchEdge) - 3 
  print("Rotations: " + str(rotations)) #This doesn't work. Reversedness isn't checked. 
  #Reversedness. If the matchEdge is greater than 3, add a reversed flag and increase the number to subtract by 4.
  
  print(edgeDict[next].index(matchEdge)) #Only need to reference this on the first run.
  print(edgeDict[nextMatch].index(matchEdge))
  print("First corner is: " + str(next))        ##Print test
  print("(0,1) is: " + str(nextMatch))          ##Print test

  #Object tile: [tilenumber, rotation (90 degrees clockwise), reversed]
  tilemap[0].append([next, False, 0])
  print(tilemap)













  while matches:
    #Both the reversed and non-reverse will match. Better to take the non-reverse and only flip the entire row if we find that we need to on the next go.
    #We know that once we get the first edge of row 2, the orientation will be locked.
    print (matchEdge)
    break
#So we know which direction to go.
#Now, if the match is on 0 (N), we know to look for nextMatch's edgeDict[1] (S). If the match is 2 (W), we know to look for 3.
#Pop next. Append next to the master list, sublist depth. Indicate needed rotations to make it go east.
#next = nextMatch. nextMatch = match for match in matches[next] if edgeDict[next][x] in edgeDict[match]. 
#If depth == 0 and len(matches[nextMatch]) == 2, you've hit the wall. Increment depth, check to see if it needs flipping, and start going west.
#If depth > 0 and len(matches[nextMatch]) == 3, repeat. THEN, if len(matches[nextRow]) == 2, you've hit the final row. Which, yay? Might not really matter.


#Find the next tile, store it and what needs to be done to it, then use that info to find the next tile.
#Corner found and arbitrary next is found. Figure out the orientation of corner such that it fits into the NW, then the orientation of next, then find next. 
#Store it in a 2d array of tuples? 


#Get the first corner to start this whole shebang off.
def getCorner(matches):
  for key, val in matches.items():
    if len(val) == 2:
      corner = key
      nextMatch = val[0]
      return corner, nextMatch

#Figure out what the next tile is sequentially based on the position of the match. Be sure to store what modifications the tiles need 
def getNext():
  return None

#Use the tile data (number, reversed = False, rotate = 0) to add data to 
def makeMap():
  return None

#Adds a tile to the map.
def addTile(number, matchEdge, targetDirection):
  return None

#Rotate a tile 90 degrees clockwise or counterclockwise. Should also be able to rotate the map in the final go.
def rotate():
  return None

#Reverse a tile on the horizontal or vertical axis. Should also be able to reverse the map in the final go.
def reverse():
  return None


edgeDict, matches = part1()
part2(edgeDict, matches)