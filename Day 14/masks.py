with open("bitmask") as file:
  instructions = [i.strip() for i in file]

"""#Part 1
memory = {}
mask = ["0" * 36] 
print(mask)

for i in instructions:
  if i[1] == "a":
    mask = i.split("=")[1].strip()
  else:
    i = i.split("=")
    address = i[0][i[0].find("[") + 1:-2]
    binValue = bin(int(i[1]))[2:]
    fullValue = "0" * (36 - len(binValue)) + binValue
    for i in range(len(fullValue)):
      if mask[i] != "X":
        fullValue = fullValue[:i] + mask[i] + fullValue[i + 1:]
    memory[address] = fullValue

answer = 0
for a in memory:
  answer += int(memory[a], 2)
print(answer)
"""
#Part 2
def computeAddrs(bAddr, mask):
  for i in range(len(bAddr)):
    if mask[i] != "0":
      bAddr = bAddr[:i] + mask[i] + bAddr[i+1:]

  addrList = [bAddr]
  for i in range(len(bAddr)):
    if bAddr[i] == "X":
      for j in range(len(addrList)):
        addrList[j] = addrList[j][:i] + "1" + addrList[j][i+1:]
        addrList.append(addrList[j][:i] + "0" + addrList[j][i+1:])

  return addrList

def intTo32b(i):
  binNum = bin(int(i[i.find("[") + 1:-2]))[2:]
  return "0" * (36 - len(binNum)) + binNum

memory = {}
mask = ["0" * 36]

for i in instructions:
  if i[1] == "a":
    mask = i.split("=")[1].strip()
  else:
    i = i.split("=")
    value = int(i[1])
    bAddr = intTo32b(i[0])
    addrList = computeAddrs(bAddr, mask)
    for addr in addrList:
      memory[int(addr, 2)] = value

print(sum(memory[a] for a in memory))