with open("bootcode") as file:
  bootcode = [i.split() for i in file]

#Part 1
def runCode(bootcode):
  repeated = [None] * len(bootcode)
  opPtr = 0
  accumulator = 0

  while repeated[opPtr] is None:
    operation = bootcode[opPtr][0]
    argument = int(bootcode[opPtr][1])
    repeated[opPtr] = 1
    #Perform ops:
    if operation == "acc":
      accumulator += argument
      opPtr += 1
    elif operation == "jmp":
      opPtr += argument
    elif operation == "nop":
      opPtr += 1
    else:
      return -1
    if opPtr == len(repeated):
      print("Code executed successfully.")
      print(accumulator)
      return 1
  print(accumulator)    
  return -1

#Part 1
runCode(bootcode)

#part 2
for code in bootcode:
  if code[0] == "nop":
    code[0] = "jmp"
    if runCode(bootcode) == 1:
      break
    code[0] = "nop"
  elif code[0] == "jmp":
    code[0] = "nop"
    if runCode(bootcode) == 1:
      break
    code[0] = "jmp"