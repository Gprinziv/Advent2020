with open("homework") as file:
  equations = [i.strip() for i in file]

#If you find a parenthesis, you need to find the matching end. If you find another one, you need to keep going, etc.

def evaluate(equ):
  i = 0
  while i < len(equ):
    if equ[i] == "(":
      depth = 1
      j = i
      while depth > 0:
        j += 1
        if equ[j] == ")":
          depth -= 1
        elif equ[j] == "(":
          depth += 1
      equ = equ[:i] + evaluate(equ[i+1:j]) + equ[j+1:]
    i += 1

  sEqu = equ.split()
  #Part 2
  i = 0
  while i < len(sEqu):
    if sEqu[i] == "+":
      sEqu[i-1] = str(int(sEqu.pop(i+1)) + int(sEqu.pop(i-1)))
    else:
      i += 1  
  i = 0
  while i < len(sEqu):
    if sEqu[i] == "*":
      sEqu[i - 1] = str(int(sEqu.pop(i+1)) * int(sEqu.pop(i-1)))
    else:
      i += 1  

  return sEqu[0]

  """#Part 1
  total = int(sEqu[0])
  for i in range(len(sEqu)):
    if sEqu[i] == "+":
      total += int(sEqu[i+1])
    elif sEqu[i] == "*":
      total *= int(sEqu[i+1])
  
  return str(total)
  """

"""
#Testing
for i in equations:
  print(i)
  print(evaluate(i))
"""
#Sum
total = 0
for i in equations:
  total += int(evaluate(i))
print(total)
