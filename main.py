with open("busTest1") as file:
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

#Compute the sum of the congruence equations
for route in listORoutes:
  for i in range(route):
    if i*route == listORoutes[route]:
      a = i * route
  #compute inverse of congruence equation x = listORoutes[route] % route (Extended Euclid Algo?)
  a = 0
  answer += (lcm / route) * listORoutes[route] * a

print(answer)
  