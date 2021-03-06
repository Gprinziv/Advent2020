with open("message3") as file:
  raw = file.read().split("\n\n")
  rawRules = [i.strip().split(":") for i in raw[0].split("\n")]
  messages = raw[1].split("\n")

rules = {}
for rule in rawRules:
  if "\"" in rule[1]:
    rules[int(rule[0])] = rule[1].lstrip(" \"").strip(" \"")
  elif "|" not in rule[1]:
    rules[int(rule[0])] = rule[1].strip().split()
  else:
    rules[int(rule[0])] = [i.lstrip().strip().split() for i in rule[1].split("|")]

for ruleIdx in rules:
  subrule = rules[ruleIdx]
  if type(subrule) == str:
    pass
  elif type(subrule[0]) == str:
    for i in range(len(subrule)):
      subrule[i] = rules[int(subrule[i])]
  else:
    for i in range(len(subrule)):
      for j in range(len(subrule[i])):
        subrule[i][j] = rules[int(subrule[i][j])]

print(rules[0])

def decode(grok):
  for smallGrok in grok:
    pass

decode(rules[0])
print(rules[0])