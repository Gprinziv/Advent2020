def makeRules(fn):
  with open(fn) as file:
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
  print("Printing Rules")
  for rule in rulesDict:
    print(str(rule) + ": " + str(rulesDict[rule]))
  print("Done.")

def isvalid(rule0, message):
  ptrs = [0]
  mPtr = [0]

  
  if len(message) > 24:
    return False
  #Cheating. Figure out how to evaluate this tbh. Can use this in conjunction with knowing the length to modify rule 0 by that many loopy subrules to get what I need?
  #We know Rule 0 is 8 11. Therefore: rule0 = z*42 y*31
  elif len(message) < 24:
    return False

  while ptrs:
    #there's something wrong here. Shit is making some weird size error no match thingies.
    if mPtr[0] >= len(message):
      #print(message + ": Success")
      return True

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
  #print(message + ": No matches")
  return False

#Input: [4, 1, 5]
#Output: "a[[aa|bb][ab|ba]|[ab|ba][aa|bb]]b"
def getRule(ruleIdx):
  global rulesDict
  rule = rulesDict[ruleIdx]
  while not all(type(x) == str for x in rule):
    i = 0
    if type(rule[0]) == list:
        rule = ["["] + rule[0] + ["|"] + rule[1] + ["]"]

    while i < len(rule):
      instruction = rule[i]
      #print(str(i) + ": " + str(instruction))
      if type(instruction) == str:
        pass
      else:
        newInst = rulesDict[instruction]
        if type(newInst) == int or type(newInst) == str:
          rule = rule[:i] + [newInst] + rule[i + 1:]
        else:
          if type(newInst[0]) == int:
            rule = rule[:i] + newInst + rule[i + 1:]
          else:
            rule = rule[:i] + ["["] + newInst[0] + ["|"] + newInst[1] + ["]"] + rule[i + 1:]
      i += 1

  rule = "".join(rule)
  return rule

def part2():
  rule42 = getRule(42)
  rule31 = getRule(31)
  #Okay so if we know what 42 and 31 evaluate to independently, we can search for any string that is 42 + 42*x + 31 using.. regex?
  #ORRRRR you could evaluate 42, save progress, then repeat. Once it fails, go back and evaluate against 8 until it fails.
  #Issue now is size checking or bound checking.
  #Epihpany!
  pass

rulesDict, messages = makeRules("message")
rule0 = getRule(0)
total = sum(isvalid(rule0, message) for message in messages)
print("Final count: " + str(total))

part2()