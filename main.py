with open("tiletest") as file:
  tiles = [x.split("\n") for x in file.read().split("\n\n")]
  for i in range(len(tiles)):
    tiles[i] = [int(tiles[i][0].split(" ")[1][:-1]), tiles[i][1:]]

edgeDict = {}
matches = {}

for tile in tiles:
  left =  "".join(tile[1][i][0] for i in range(len(tile[1])))
  right = "".join(tile[1][i][-1] for i in range(len(tile[1])))
  edgeDict[tile[0]] = [tile[1][0], tile[1][-1], left, right, tile[1][0][::-1], tile[1][-1][::-1], left[::-1], right[::-1]]
  matches[tile[0]] = []

for i in range(len(tiles)):
  for j in range(i + 1, len(tiles)):
    if set(edgeDict[tiles[i][0]]) & set(edgeDict[tiles[j][0]]):
      matches[tiles[i][0]].append(tiles[j][0])
      matches[tiles[j][0]].append(tiles[i][0])

total = 1
for tile, match in matches.items():
  if len(match) == 2:
    print(tile)
    total *= tile
print(total)

#Go through each tile and find left/right matches along a singular axis.
#Repeat from that tile on the other axis. Then advance along one axis and fill in the tiles, I guess.

#Need to take that edge dict and actually figure out what the correct orientation of each tile is, then join the strings to make a superstring. (It's a 12x12 tile (120 char x 120 char))
#Once that's done, scan for sea monsters in each orientation (change monster orientation on each check, not the image). Finding a hit means it's the correct orientation.
#Once that's been done, iterate through the image and convert sea monster hits into Os
#Finally, count the number of #s that remain.