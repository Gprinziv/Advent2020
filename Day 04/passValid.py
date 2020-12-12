import re, string
with open("passports") as file:
  passes = file.read().split("\n\n")

def validPassport(passport):
  if len(passport) not in range(7, 9) or (len(passport) == 7 and "cid" in passport):
    return False
  if int(passport["byr"]) not in range(1920, 2003):
    return False
  if int(passport["iyr"]) not in range(2010, 2021):
    return False
  if int(passport["eyr"]) not in range(2020, 2031):
    return False
  if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
    return False
  if len(passport["pid"]) != 9 or not passport["pid"].isnumeric():
    return False

  height = passport["hgt"]
  if height[-2:] == "cm":
    if int(height[:-2]) not in range(150, 194):
      return False
  elif height[-2:] == "in":
    if int(height[:-2]) not in range(59, 77):
      return False
  else:
    return False

  hair = passport["hcl"]
  if len(hair) != 7 or hair[0] != "#":
    return False
  for digit in hair[1:]:
    if digit not in string.hexdigits:
      return False
  
  print("PID:" + passport["pid"])
  return True

numValid = 0
for passport in passes:
  fields = re.split(":| |\n", passport)
  fields = {fields[i] : fields[i + 1] for i in range(0, len(fields), 2)}
  if validPassport(fields):
    numValid += 1

print(numValid)