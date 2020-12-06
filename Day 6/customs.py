with open("customs") as file:
  groups = file.read().split("\n\n")

lowers = "abcdefghijklmnopqrstuvwxyz"

#part 1
totalSum = 0
for group in groups:
  groupSum = 0
  for letter in lowers:
    if letter in group:
      groupSum += 1
  totalSum += groupSum
print(totalSum)

#part 2
totalSum = 0
for group in groups:
  groupSize = group.count("\n") + 1
  groupSum = 0
  for letter in lowers:
    if group.count(letter) == groupSize:
      groupSum += 1
  totalSum += groupSum
print(totalSum)