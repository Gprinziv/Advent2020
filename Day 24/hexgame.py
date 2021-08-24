with open("teststart") as file:
  start = [[int(cell) for cell in row.lstrip().split("  ")] for row in file.read().split("\n")[:-1]]

#Each generation: If there's a number active on the borders, make a new row/column. then play the game of life.
def expand(arr):
  if any(i[0] == 1 for i in arr):
    for i in range(len(arr)):
      arr[i].insert(0, 0)
  if any(i[-1] == 1 for i in arr):
    for i in range(len(arr)):
      arr[i].append(0)
  if 1 in arr[0]:
    arr.insert(0, [0 for i in arr[0]])
  if 1 in arr[-1]:
    arr.append([0 for i in arr[0]])
  return arr

def generation(arr):
  arr = expand(arr)
  #Special Adjacency:
  #Rows with odd indexes are "offset" by 0.5.
  #odds =  [L, U, UR, R, DR, D]
  #evens = [R, U, UL, L, DL, D]
  U, UR, R, DR  = (-1,0), (-1,1), (0,1), (1,1)
  D, DL, L, UL = (1,0), (1,-1), (0,-1), (-1,-1)

  newarr = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]

  for i in range(len(arr)):
    if i == 0:
      setL = [R, D]
      setR = [L, DL, D]
      setM = [L, DL, D, R]
    elif i == len(arr) - 1:
      if i % 2 == 0:
        setL = [U, R]
        setR = [U, UL, L]
        setM = [L, UL, U, R]
      else:
        setL = [U, UR, R]
        setR = [U, L]
        setM = [R, UR, U, L]
    elif i % 2 == 0:
      setL = [U, R, D]
      setR = [U, UL, L, DL, D]
      setM = [R, U, UL, L, DL, D]
    else:
      setL = [U, UR, R, DR, D]
      setR = [U, L, D]
      setM = [L, U, UR, R, DR, D]

    countL = sum(arr[i + y][x] for y, x in setL)
    countR = sum(arr[i + y][x - 1] for y, x in setR)
  
    for j in range(1, len(arr[0]) - 1):
      countM = sum(arr[i + y][j + x] for y, x in setM)
      if (arr[i][j] == 0 and countM == 2) or (arr[i][j] == 1 and countM in (1,2)):
        newarr[i][j] = 1

    if (arr[i][0] == 0 and countL == 2) or (arr[i][0] == 1 and countL in (1,2)):
      newarr[i][0] = 1
    if (arr[i][-1] == 0 and countR == 2) or (arr[i][-1] == 1 and countR in (1,2)):
      newarr[i][-1] = 1

  return newarr

for row in start:
  print(row)
for i in range(100):
  start = generation(start)
  total = 0
  for row in start:
    total += sum(cell for cell in row)
  print("Day " + str(1 + i) + " total: " + str(total)) 