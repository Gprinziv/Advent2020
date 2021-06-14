#Cup preset constants for makeDict
SAMPLE = 389125467
PUZZLE = 562893147
INPUT = PUZZLE

#Game size and turn count constants
PART = 2
NUMCUPS = 9 if PART == 1 else 1000000
ENDGAME = 100 if PART == 1 else 10000000


def moveCups(cupDict, curCup):
  r1 = cupDict[curCup]
  r2 = cupDict[r1]
  r3 = cupDict[r2]
  removed = [curCup, r1, r2, r3]
  destination = curCup
  while destination in removed:
    destination = destination - 1 if destination > 1 else NUMCUPS

  cupDict[curCup] = cupDict[r3]
  cupDict[r3] = cupDict[destination]
  cupDict[destination] = r1

  return cupDict

#prints the cups in a way similar to the example, but doesn't play nice when 3 is removed.
def printCups(cupDict, curCup):
  firstCup = str(INPUT)[0]
  cups = [firstCup]
  nextCup = cupDict[int(firstCup)]

  while nextCup != int(firstCup):
    if nextCup == curCup:
      cups.append("(" + str(nextCup) + ")")
    else:
      cups.append(" " + str(nextCup) + " ")
    nextCup = cupDict[nextCup]
  
  print("".join(cups))

#Accepts which part you're currently working on as input
#Returns a dictionary of cups and the number of the cup immediately to its left.
def makeDict():
  nextCup = {}
  cupString = str(INPUT)

  for i in range(len(cupString) - 1):
    nextCup[int(cupString[i])] = int(cupString[i+1])

  if PART == 1:
    nextCup[int(cupString[-1])] = int(cupString[0])
  else:
    nextCup[int(cupString[-1])] = len(cupString) + 1
    for i in range(len(cupString) + 1, NUMCUPS):
      nextCup[i] = i+1
    nextCup[NUMCUPS] = int(cupString[0])

  return nextCup, int(cupString[0])

def main():
  cupDict, curCup = makeDict()
  move = 0
  while move < ENDGAME:
    move += 1
    if PART == 1:
      print("-- Move " + str(move) + " --")
      printCups(cupDict, curCup)
    elif move % 1000000 == 0:
      print("-- Move " + str(move) + " --")

    cupDict = moveCups(cupDict, curCup)
    curCup = cupDict[curCup]
  print("-- Final -- ")

  if PART == 1:
    nextCup = cupDict[1]
    labels = ""
    while nextCup != 1:
      labels += str(nextCup)
      nextCup = cupDict[nextCup]
    print(labels)
  else:
    mplicand = cupDict[1]
    mplier = cupDict[mplicand]
    print(mplier * mplicand)


if __name__ == "__main__":
  main()

"""
#Old prints:
  print("-- Move " + str(move) + " --")
  print("-- Final -- ")
  print("Current cup: " + str(curCup))
  print("Destination: " + str(destination))
  print("Removed: " + str(removed[1:]))
"""