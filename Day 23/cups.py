SAMPLE = 32415
SAMPLE2 = 389125467
INPUT = 562893147
ENDGAME = 100

order = [int(n) for n in str(INPUT)]
move = 0

def moveCups(order):
  curCup = order[0]
  removed = order[1:4]

  destination = curCup - 1
  if destination == 0:
    destination = len(order)
  while True:
    if destination not in removed:
      break
    destination = destination - 1
    if destination == 0:
      destination = len(order)

  print("Cup order: " + str(order))
  print("Removed: " + str(removed))
  print("Destination: " + str(destination) + "\n")

  order = order[4:desIndex + 1] + removed + order[desIndex + 1:] + [order[0]]
  return order

while move < ENDGAME:
  move += 1
  print(" -- Move " + str(move) + " --")
  order = moveCups(order)

print("-- Final -- ")
print(order)
idx = order.index(1)
finalOrder = order[idx+1:] + order[:idx]
print("".join(str(n) for n in finalOrder))