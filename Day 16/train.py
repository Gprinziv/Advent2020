with open("tickets") as file:
  rules = file.read().split("\n\n")

#total = 0
yourTkt = [int(i) for i in rules[1].split("\n")[1].split(",")]
othrTkt = [i for i in rules[2].split("\n")[1:]]
fRules = [i.split() for i in rules[0].split("\n")]
rules = {}
for rule in fRules:
  if len(rule) == 5:
    rules[rule[0] + " " + rule[1][:-1]] = [int(i) for i in rule[-3].split("-")] + [int(i) for i in rule[-1].split("-")]
  else:
    rules[rule[0][:-1]] = [int(i) for i in rule[-3].split("-")] + [int(i) for i in rule[-1].split("-")]

toPop = []
for ticket in othrTkt:
  vals = [int(i) for i in ticket.split(",")]

  for val in vals:
    valid = False

    for rule in rules:
      if rules[rule][0] <= val <= rules[rule][1] or rules[rule][2] <= val <= rules[rule][3]:
        valid = True

    if valid == False:
      #total += val
      toPop.append(othrTkt.index(ticket))
      break
for index in sorted(toPop, reverse=True):
  othrTkt.pop(index)

cans = {i : [] for i in rules}
for rule in rules:
  for i in range(len(rules)):
    valid = True
    for ticket in othrTkt:
      val = int(ticket.split(",")[i])
      if val < rules[rule][0] or rules[rule][1] < val < rules[rule][2] or rules[rule][3] < val:
        valid = False
        break
    if valid == True:
        cans[rule].append(i)

final = {}
while cans:
  for can in cans:
    if len(cans[can]) == 1:
      final[can] = cans[can][0]
      cans.pop(can)
      for can2 in cans:
        if final[can] in cans[can2]:
          cans[can2].remove(final[can])
      break

total = 1
for rule in final:
  if len(rule) >= 9 and rule[:9] == "departure":
    total *= yourTkt[final[rule]]

print(total)