with open("message3") as file:
  raw = file.read().split("\n\n")
  rawRules = [i.strip().split(":") for i in raw[0].split("\n")]
  messages = raw[1].split("\n")

#Generate a human-readable dictionary to store and access the rules for later.
rulesDict = {}
for rule in rawRules:
  if "\"" in rule[1]:
    rulesDict[int(rule[0])] = rule[1].lstrip(" \"").strip(" \"")
  elif "|" not in rule[1]:
    rulesDict[int(rule[0])] = rule[1].strip().split()
  else:
    rulesDict[int(rule[0])] = [i.lstrip().strip().split() for i in rule[1].split("|")]

#Regular Expressions?




""" Recursive solution. Works only for small data sets.
#Generate a human-readable dictionary to store and access the rules for later.
rulesDict = {}
for rule in rawRules:
  if "\"" in rule[1]:
    rulesDict[int(rule[0])] = rule[1].lstrip(" \"").strip(" \"")
  elif "|" not in rule[1]:
    rulesDict[int(rule[0])] = rule[1].strip().split()
  else:
    rulesDict[int(rule[0])] = [i.lstrip().strip().split() for i in rule[1].split("|")]


#Using a dictionary of rules, it translates whatever the current rule you're looking at.
#Rules are a list with some combination of strings or lists.
#Read a rule sequentially.
#If the current instruction is a string object, simply append it to each password.
#If the current instruction is a list object, copy the password for each item in the list, then decode.
#Result will be a list of unjoined strings.
def decode(rule, rulesDict):
  passList = [[]]
  for instruction in rule:
    subrule = rulesDict[int(instruction)]
    if type(subrule) == str:
      for password in passList:
        password.append(subrule)
    else:
      tempList = []
      for password in passList:
        for subsubrule in subrule:
          for s in decode(subsubrule, rulesDict):
            tempList.append(password + s)
      passList = tempList
  return passList 

finalList = decode(rulesDict[0], rulesDict)
passwords = []
for f in finalList:
  passwords.append("".join(f))
print(passwords)
print(messages)

print(sum(i == j for i in passwords for j in messages))
"""