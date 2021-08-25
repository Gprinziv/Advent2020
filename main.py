with open("message") as file:
  raw = file.read().split("\n\n")
rulesDict = {}
for rule in raw[0].split("\n"):
  rule = rule.split(":")
  if "\"" in rule[1]:
    subrules = rule[1][2]
  elif "|" in rule[1]:
    subrules = [[int(j)for j in i.strip().split()] for i in rule[1].strip().split("|")]
  else:
    subrules = [[int(i) for i in rule[1].strip().split(" ")]]
  rulesDict[int(rule[0])] = subrules
messages = raw[1].split("\n")

#Print the RulesDict when necessary.
for rule in rulesDict:
  if len(rulesDict[rule]) == 1:
    print(str(rule) + ": " + str(rulesDict[rule]))

#Input: The rule in rulesDict to be evaluated.
#Output: The list of passwords (or password fragments) that match the completely evaluated rule.
def decode2(rule):
  global rulesDict
  passList = [[]]
  instructions = rulesDict[rule]
  return None
  #Instructions can be:
    #Len 2:
      #A list containing two lists of two integers
      #A list contianing two lists of one integer
    #Len 1:
      #A list containing one integer
      #A list containing two integers

  #If the rule is just a string, add that string to every password in the passList.
  if type(instructions) == str:
    for password in passList:
      password.append(instructions)
  #If the rule has only one element (No split).
  elif len(instructions) == 1:
    for item in instructions: #Exavluate the items linearly. Evaluate e1 and append it to all extant passwords. Then evaluate e2 and do the same.
      pass #Decode each item and append that to the password without making more.
  else: #it's a list with two elements (A split).
    for split in instructions: #There's a split, so each one has to be its own password branch. Create a temp list, then append the results of each split to each password (doubling the total number of passwords)
      pass  

  return None #Remove in final.

#RECURSION PART 2! Now with incompatable rules input!
#Passlist creates a list of all possible passwords, then compare 
def decode(rule):
  global rulesDict
  passList = [[]]
  print(rule)
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

#finalList = decode(rulesDict[0])
finalList = decode2(0)
passwords = []
for f in finalList:
  passwords.append("".join(f))
print(passwords)
print(messages)

print(sum(i == j for i in passwords for j in messages))


def linearSolve():
  """
  #Need to format Rule 0 into a string like: "abbb[ab|ba][[ba|ab]b|a[bb|aa]]baa"
  #Consider shelving the current logic and just working on the second half, and bridge it later.
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

  rule0 = "a[[aa|bb][ab|ba]|[ab|ba][aa|bb]]b"
  total = sum(isvalid(rule0, message) for message in messages)
  print(total)
  """
  return None