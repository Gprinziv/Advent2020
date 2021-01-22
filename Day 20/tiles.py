with open("tiletest") as file:
  tiles = [x.split("\n") for x in file.read().split("\n\n")]

for tile in tiles:
  for row in tile:
    print(row)
  print("\n")

  #Choose a tile to be tile 1, test all remaining tiles against the leftmost edge.
  #Any time there's a match, test all *other* tiles against that leftmost edge.
  #Repeat until all 9 tiles have been matched, then return that arrangement.