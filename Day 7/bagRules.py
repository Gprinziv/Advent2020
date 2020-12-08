with open("regulations") as file:
  bagRules = [i.strip().split(maxsplit=2) for i in file]
for i in range(len(bagRules)):
  bagRules[i][0] += " " + bagRules[i].pop(1)

"""
#part 1
bagQueue = ["shiny gold"]
canHoldGold = []
while bagQueue:
  bag = bagQueue.pop(0)
  for rule in bagRules:
    ruleStr = rule[0] + " " + rule[1]
    if bag in rule[2] and ruleStr not in canHoldGold:
      bagQueue.append(ruleStr)
      canHoldGold.append(ruleStr)

print(len(canHoldGold))
"""

def findBags(bag):
  totalBags = 0

  #Find the matching rule in the list of rules.
  for bagRule in bagRules:
    if bagRule[0] == bag:
      if "no other" in bagRule[1]:
        print(bag + " contains itself.")
        return 1
      insideBag = bagRule[1][13:-1].split()
      insideBag = {insideBag[i+1] + " " + insideBag[i+2] : int(insideBag[i]) for i in range(0, len(insideBag), 4)}
      break 

  print(bag + " contains " + str(insideBag))
  for bag in insideBag:
    totalBags += (insideBag[bag] * findBags(bag))
    print("Total bags in " + bag + ": " + str(totalBags))
  #need to convert this string into a series of tokens for use.
  return 1 + totalBags

print(findBags("shiny gold"))
