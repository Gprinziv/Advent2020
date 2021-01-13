import copy
with open("decks") as file:
  decks = [i for i in file.read().split("\n\n")]
p1 = [int(i.strip()) for i in decks[0].split("\n")[1:]]
p2 = [int(i.strip()) for i in decks[1].split("\n")[1:]]

#Part 1
def combat(p1, p2):
  round = 0
  while p1 and p2:
    round += 1
    card1 = p1.pop(0)
    card2 = p2.pop(0)
    if card1 > card2:
      p1.append(card1)
      p1.append(card2)
    else:
      p2.append(card2)
      p2.append(card1)

  if p1:
    return p1
  else:
    return p2

#Part 2
def reCombat(p1, p2, subgame = False):
  if subgame:
    p1 = copy.deepcopy(p1)
    p2 = copy.deepcopy(p2)
  states = set()

  while p1 and p2:
    if (tuple(p1), tuple(p2)) in states:
      return 1 if subgame else p1

    states.add((tuple(p1), tuple(p2)))
    card1 = p1.pop(0)
    card2 = p2.pop(0)
    if len(p1) >= card1 and len(p2) >= card2:
      winner = reCombat(p1[:card1], p2[:card2], True)
    else:
      winner = 1 if card1 > card2 else 2

    if winner == 1:
      p1.append(card1)
      p1.append(card2)
    else:
      p2.append(card2)
      p2.append(card1)

  winner = 1 if p1 else 2
  if subgame:
    return 1 if p1 else 2
  else:
    return p1 if p1 else p2

def score(deck):
  total = 0
  for i, val in enumerate(reversed(deck), start = 1):
    total += i * val
  return total

#part 1
#print(score(combat(p1, p2)))

#part 2
print("Start")
print(score(reCombat(p1, p2)))
print(p1)
print(p2)