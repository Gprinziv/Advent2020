import itertools
with open("xmas") as file:
  xmas = [int(i) for i in file]
last25 = [xmas[i] for i in range(25)]

for i in range(25, len(xmas)):
  for combos in itertools.combinations(last25, 2):
    if sum(combos) == xmas[i]:
      last25.append(xmas[i])
      break
  if len(last25) == 26:
    last25.pop(0)
  else:
    print("Nonsum number found! Value: " + str(xmas[i]))
    targetAddress = i
    targetNumber = xmas[i]
    break

#Part 2
for i in range(targetAddress):
  curSum = xmas[i]
  for j in range(i + 1, targetAddress):
    curSum += xmas[j]
    if curSum > targetNumber:
      break 
    elif curSum == targetNumber:
      weakness = sorted([xmas[r] for r in range(i, j + 1)])
      print(weakness[0] + weakness[-1])