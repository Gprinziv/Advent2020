with open("passwords") as file:
  pwList = [i for i in file]

numValid = 0

#Part 1
"""
for line in pwList:
  pwLine = line.split()
  minMax = pwLine[0].split('-')

  if int(minMax[0]) <= pwLine[2].count(pwLine[1][0]) <= int(minMax[1]):
    numValid += 1

print(numValid)
"""

for line in pwList:
  pwLine = line.split()
  ab = [(int(i) - 1) for i in pwLine[0].split("-")]
  chk = pwLine[1][0]
  a = bool(chk == pwLine[2][ab[0]])
  b = bool(chk == pwLine[2][ab[1]])
  if (a and not b) or (b and not a):
    numValid += 1

print(numValid)