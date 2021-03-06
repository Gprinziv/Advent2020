with open("message") as file:
  raw = file.read().split("\n\n")
  rawRules = [i.strip().split(":") for i in raw[0].split("\n")]
  messages = raw[1].split("\n")

#Operate on the current valid rule.
def operate(rules, valids, i):
  valid = valids[i]
  temp = []
  added = False
  for j in range(len(valid)):
    subrule = valid[j]
    if type(subrule) == str:
      temp.append(subrule)
    else:
      newRule = rules[subrule]
      if type(newRule) == str:
        temp.append(newRule)
      else:
        if len(newRule) > 1:
          for newSub in newRule[1:]:
            newValid = temp.copy() + [int(i) for i in newSub.split()] + valid[j+1:]
            valids.append(newValid)
            added = True
        temp.extend([int(i) for i in newRule[0].split()])
  valids[i] = temp
  return added

#Convert the rules list to a better structure. All subrules will be a tuple or a letter.
rules = {}
for rule in rawRules:
  if "\"" in rule[1]:
    rules[int(rule[0])] = rule[1].lstrip(" \"").strip(" \"") 
  else:
   rules[int(rule[0])] = tuple(i.strip().lstrip() for i in rule[1].split("|"))

#Start with rule 0.
valids = []
for rule in rules[0]:
  valids.append([int(i) for i in rule.split()])

while True:
  finish = True

  for i in range(len(valids)): #for each rule in the master list of rules
    added = operate(rules, valids, i)

    if added:
      finish = False
    for subrule in valids[i]:
      if type(subrule) == int:
        finish = False

  if finish:
    break

for i in range(len(valids)):
  valids[i] = "".join(valids[i])

total = 0
for message in messages:
  if any(valid == message for valid in valids):
    total += 1

print(total)