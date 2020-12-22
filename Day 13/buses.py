with open("buses") as file:
  routes = [i.strip() for i in file]

print(routes)

"""
#Part 1
bestTime = int(routes[0])
bestRoute = 0
for route in routes[1].split(","):
  if route.isdecimal():
    busTime = int(route) - (int(routes[0]) % int(route))
    if busTime < bestTime:
      bestTime = busTime
      bestRoute = int(route)

print(bestRoute * bestTime)
print(bestTime)
print(bestRoute)
"""
#Part 2
#Oops all Chinese remainders
schedule = routes[1].split(",")
lcm = 1
offset = 0
listORoutes = {}
answer = 0

#Populate our congurence equation.
for route in schedule:
  if route == "x":
    offset += 1
  else:
    listORoutes[int(route)] = offset
    lcm *= int(route)
    offset +=1

print(listORoutes)
print(lcm)

#Cinese Remainder Theorum:
#The answer to a series of coprime (gcd of all routes = 1) congruence equations is
#the sum of b(i)N(i)x(i), where b is the remainder of the modulo, N is the (lcm / modulo)
#and x(i) is the inverse of N(i) such that N(i)x(i) = 1 (% modulo)
for route in listORoutes:
  print(route)
  #x(route) = (lcm / route) * x % route == 1, 0<=x<route
  for x in range(route):
    if lcm/route * x % route == 1:
      answer += lcm // route * listORoutes[route] * x
      break

print(-answer%lcm)