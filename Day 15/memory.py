with open("starter") as file:
  history = [int(i) for i in file.read().split(",")]

#limit = 2020
limit = 30000000

ages = {}
turn = 0

for num in history[:-1]:
  turn += 1
  ages[num] = turn
  speak = num

turn += 1
speak = history[-1]

while(turn < limit):
  turn += 1
  if turn % 1000000 == 0:
    print(turn)
  if speak not in ages:
    ages[speak] = turn - 1
    speak = 0
  else:
    temp = speak
    speak = turn - 1 - ages[speak]
    ages[temp] = turn - 1

print(speak)