#Part 1
def calcPos(posStr, minLtr):
  minPos = 0
  maxPos = 2**len(posStr) - 1
  for letter in posStr:
    if letter == minLtr:
      maxPos = int((minPos + maxPos) / 2)
    else:
      minPos = int((minPos + maxPos) / 2) + 1
  return maxPos

with open("passes") as file:
  passes = [i.strip() for i in file]

order = {'F': 0, 'B': 1, 'L': 2, 'R': 3}
passes.sort(key = lambda word: [order.get(c, ord(c)) for c in word])

#Part 1
#print(calcPos(passes[-1][:7], "F") * 8 + calcPos(passes[-1][7:], "L"))

#Part 2. Get the range. Then start cutting it in half and finding the smaller  
minSID = calcPos(passes[0][:7], "F") * 8 + calcPos(passes[0][7:], "L")
maxSID = calcPos(passes[-1][:7], "F") * 8 + calcPos(passes[-1][7:], "L")
print(minSID)
print(maxSID)

for i in range(0, len(passes)):
  SID = calcPos(passes[i][:7], "F") * 8 + calcPos(passes[i][7:], "L")
  print("SID is: " + str(SID))
  if SID != i + minSID:
    print(i + minSID)
    break