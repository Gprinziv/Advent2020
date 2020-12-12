with open("slope") as file:
  slopes = [i.strip() for i in file]
#Part 1
"""
x=0
treeCount = 0
for row in slopes:
  if row[x] == '#':
    treeCount += 1
  x = (x + 3) % len(row)

print(treeCount)
"""
#Part 2
def treeCount(across, down):
  x = 0
  y = 0
  treeCount = 0

  for row in slopes:
    if y == 0:
      if row[x] == '#':
        treeCount += 1
      x = (x + across) % (len(row))
    y = (y + 1) % down
  return treeCount

print(treeCount(1, 1))
print(treeCount(3, 1))
print(treeCount(5, 1))
print(treeCount(7, 1))
print(treeCount(1, 2))

print(treeCount(1, 1) * treeCount(3, 1) * treeCount(5, 1) * treeCount(7, 1) * treeCount(1, 2))