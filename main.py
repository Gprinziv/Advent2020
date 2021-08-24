with open("message") as file:
  raw = file.read().split("\n\n")

rulesDict = {}
for rule in raw[0].split("\n"):
  rule = rule.split(":")
  if "\"" in rule[1]:
    subrules = rule[1][2]
  elif "|" in rule[1]:
    subrules = [[int(j) for j in i.strip().split()] for i in rule[1].strip().split("|")]
  else:
    subrules = [int(i) for i in rule[1].strip().split(" ")]
  rulesDict[int(rule[0])] = subrules
messages = raw[1].split("\n")


#Now we need to..... ugh, I dunno?