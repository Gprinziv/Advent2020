"""
#MAYBE: check the length of the valid messages by having the pointer iterate over the master string. Split the pointer at branches, destroy them and resume at merges.
#Remove all messages that aren't of valid length.

#Then:
#Traverse the single string and any time you get to a '[', create a second pointer. When you get to a '|'&']', merge the pointers again.
#Check each pointer against the current message string and if the pointers are invalid, delete them.
#If there are no pointers, the message fails. Return False.
#If the message has a valid pointer tha tmatches length (if there isn't one uniform length for every message), then it's valid! Return True
def isvalid(rule0, message):
  ptrs = [0]
  mPtr = 0

  while ptrs:
    i = 0
    while i < len(ptrs): #For each pointer in the list, perform one operation on it and increment it.
      cur = rule0[ptrs[i]]
      if cur.isalpha(): #If it's a simple a or b, evaluate it.
        pass
      elif cur == "[": #Create 2 pointers and operate on both immediately.
        pass
      elif cur == "|": #If cur is "|" or "]", merge the pointers. If |, go to addr:"]"+1. If "]", go to addr: cur+1 unless cur+1 in ptrs.
        pass
      else:
        if cur + 1 in ptrs:
          ptrs.pop(i)
        else:
          ptrs[i] += 1
          i += 1

    mPtr += 1
  return False
"""

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

#Need to format Rule 0 into a string like: "abbb[ab|ba][[ba|ab]b|a[bb|aa]]baa"
#Consider shelving the current l
# ogic and just working on the second half, and bridge it later.
for rule in rulesDict:
  print(str(rule) + ": " + str(rulesDict[rule]))

def decode(rule):
  global rulesDict
  passList = [[]]
  for instruction in rule:
    subrule = rulesDict[instruction]
    if type(subrule) == str:
      for password in passList:
        password.append(subrule)
    else:
      tempList = []
      for password in passList:
        for subsubrule in subrule:
          for s in decode(subsubrule):
            tempList.append(password + s)
      passList = tempList
  return passList 

finalList = decode(rulesDict[0])
passwords = []
for f in finalList:
  passwords.append("".join(f))
print(passwords)
print(messages)

print(sum(i == j for i in passwords for j in messages))



"""
rule0 = "a[[aa|bb][ab|ba]|[ab|ba][aa|bb]]b"
total = sum(isvalid(rule0, message) for message in messages)
print(total)
"""