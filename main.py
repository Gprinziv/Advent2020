import re, string
with open("passports") as file:
  passes = file.read().split("\n\n")
