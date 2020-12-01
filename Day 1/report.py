with open("report") as file:
  expReport = [int(i) for i in file]

#Part 1
"""
for x in range(len(expReport)):
  need = 2020 - expReport[x]
  for y in range(x, len(expReport)):
    if expReport[y] == need:
      print(str(expReport[x]) + ", " + str(expReport[y]))
      print (expReport[x] * expReport[y])
"""

#Part 2
for x in range(len(expReport)):
  need = 2020 - expReport[x]
  for y in range(x, len(expReport)):
    need2 = need - expReport[y]
    if need2 > 0:
      for z in range(y, len(expReport)):
        if expReport[z] == need2:
          print(str(expReport[x]) + ", " + str(expReport[y]) + ", " + str(expReport[z]))
          print (expReport[x] * expReport[y] * expReport[z])