with open("allergies") as file:
  foods = [i for i in file]

allergens = {}
ingredientList = set()
foodList = []

for food in foods:
  food = food.strip(")\n").split("(")
  ingredients = food[0].split()
  for i in ingredients:
    foodList.append(i)
    if i not in ingredientList:
      ingredientList.add(i)

  for allergen in [i.strip(",") for i in food[1].split()[1:]]:
    if allergen not in allergens:
      allergens[allergen] = set(ingredients).copy()
    else:
      allergens[allergen].intersection_update(set(ingredients))

for a in allergens:
  ingredientList.difference_update(allergens[a])

#Part 1
total = sum(foodList.count(i) for i in ingredientList)
print(total)

#Part 2
canAllergens = {}
while allergens:
  for a in list(allergens.keys()).copy():
    if len(allergens[a]) == 1:
      temp = allergens.pop(a)
      for b in allergens:
        allergens[b].difference_update(temp)
      canAllergens[a] = temp.pop()

canString = ""
for ingredient in sorted(canAllergens.keys()):
  canString += canAllergens[ingredient] + ","
print(canString.strip(","))