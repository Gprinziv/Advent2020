def makeRules():
  with open("message3") as file:
    raw = file.read().split("\n\n")
  rulesDict = {}
  for rule in raw[0].split("\n"):
    rule = rule.split(":")
    if "\"" in rule[1]:
      subrules = rule[1][2]
    elif "|" in rule[1]:
      subrules = [[int(j)for j in i.strip().split()] for i in rule[1].strip().split("|")]
    else:
      subrules = [int(i) for i in rule[1].strip().split(" ")]
    rulesDict[int(rule[0])] = subrules
  messages = raw[1].split("\n")

  return rulesDict, messages

def printRules(rulesDict):
  for rule in rulesDict:
    print(str(rule) + ": " + str(rulesDict[rule]))

def isvalid(rule0, message):
  ptrs = [0]
  mPtr = [0]

  while ptrs:
    if mPtr[0] >= len(message):
      while ptrs[0] < len(rule0):
        if rule0[ptrs[0]] != "]":
          print(message + ": Size Error")
          return False
        ptrs[0] += 1
      print(message + ": Success")
      return True
    elif ptrs[0] >= len(rule0):
      print(message + ": Size Error")
      return False

    cur = rule0[ptrs[0]] #Get the value pointed to by the current pointer
    if cur.isalpha(): #If it's a simple a or b, evaluate it. If it's bad, trash the pointers and start from the next one.
      if message[mPtr[0]] == cur:
        ptrs[0] += 1
        mPtr[0] += 1
      else:
        ptrs.pop(0)
        mPtr.pop(0)
    elif cur == "[": #Create a second pointer after the relevant "|". Watch for errant "["s. Increment pointer.
      tempPtr, depth = ptrs[0] + 1, 1
      while depth > 0:
        if rule0[tempPtr] == "[":
          depth += 1
        elif rule0[tempPtr] == "|":
          depth -= 1
        tempPtr += 1
      ptrs.append(tempPtr)
      mPtr.append(mPtr[0])
      ptrs[0] += 1
    elif cur == "|": # Skip forward to after the relevant "]". Watch for errant "["s.
      depth = 1
      while depth > 0:
        ptrs[0] += 1
        if rule0[ptrs[0]] == "[":
          depth += 1
        elif rule0[ptrs[0]] == "]":
          depth -= 1
      ptrs[0] += 1
    else: #Cur is at a "]", just increment it.
      ptrs[0] += 1

  #If you're run out of valid pointers to check, the rule must be invalid.
  print(message + ": No matches")
  return False

#Input: [4, 1, 5]
#A list of subrules to be evaluated.
#Output: "a[[aa|bb][ab|ba]|[ab|ba][aa|bb]]b"
#A string representation of the branching paths one can take.
def getRule0(rulesDict):
  while not all(type(i) == str for i in rulesDict[0]):
    for i in range(len(rulesDict[0])):
      instruction = rulesDict[0][i]
      if type(instruction) == str:
        pass
      else:
        newInst = rulesDict[instruction]
        if len(newInst) == 1:
          #then there's no split. Just plug the new thing(s) in here sequentially
          break
        else:
          #There's a split, Append ["[", i[0], "|", i[1], "]"] 
          break



    print("You got work, kiddo!")
    break
  print(rulesDict[0])
  return rulesDict[0]

rulesDict, messages = makeRules()
print(rulesDict[0])
#rulesDict[0] = "a[[aa|bb][ab|ba]|[ab|ba][aa|bb]]b"
rule0 = getRule0(rulesDict)
#total = sum(isvalid(rule0, message) for message in messages)
#print("Final count: " + str(total))