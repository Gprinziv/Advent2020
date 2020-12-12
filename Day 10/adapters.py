with open("joltages") as file:
  jolts = [int(i) for i in file]

jolts.sort()
jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)

#Part 1
diff1 = 0
diff3 = 0
diff2 = 0
for i in range(1, len(jolts)):
  if jolts[i] - jolts[i-1] == 1:
    diff1 += 1
  elif jolts[i] - jolts[i-1] == 3:
    diff3 += 1
print(diff1)
print(diff3)
print(diff1 * diff3)

#Part 2. (NOT) HAAARD
joltMap = {jolts[-1] : 1, jolts[-2] : 1, jolts[-3] : 1}
for i in range(len(jolts) - 4, -1, -1):
  combos = joltMap[jolts[i+1]] #You know the next adapter will fit
  if jolts[i+3] - jolts[i] <= 3:
    combos += joltMap[jolts[i+2]] + joltMap[jolts[i+3]]
  elif jolts[i+2] - jolts[i] <= 3:
    combos += joltMap[jolts[i+2]]
  joltMap[jolts[i]] = combos

print(joltMap[0])
#When you reach 0, that's your answer.
