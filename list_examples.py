from collections import deque
from numpy import ndarray  # VERY efficient numeric array 

list1 = list()   # empty list
list2 = ['Winken', 'Blinken', 'Nod']
list3 = []  # empty list
list4 = ['apple', 42, "mango", 5.9]

cities = ['Houston', 'Jersey City', 'Plano', 'Durham', 'Brooklyn']
print("cities: {}".format(cities))
cities.insert(0, 'Chicago')
cities.insert(3, 'Glasgow')
print("cities: {}".format(cities))
cities.append("Wilmington")
print("cities: {}".format(cities))
more_cities = ['Newark', 'Washington, DC', 'Miami']
cities.extend(more_cities)
print("cities: {}".format(cities))
# LIST.insert(pos, VALUE)  LIST.append(value)  LIST.extend(iterable)
cities[10] = "Jacksonville"
print("cities: {}".format(cities))

del cities[2]   #  del var    del LIST[0]   del DICT[key]
print("cities: {}".format(cities))
cities.remove('Durham')
print("cities: {}".format(cities))

c = cities.pop()
print("c: {}".format(c))
print("cities: {}".format(cities))

c = cities.pop(4)
print("c: {}".format(c))
print("cities: {}".format(cities))
#  del LIST[pos]  LIST.remove(value)   LIST.pop(pos=-1)
print(cities[0], cities[4], cities[-1], cities[len(cities)-1])
print(len(cities))
print(sorted(cities), '\n')
# cities.sort()
#   LIST[START:STOP]    LIST[:STOP]  LIST[START:]
print("cities: {}".format(cities))

print(cities[0:3], cities[:3])
print(cities[2:5])
print(cities[-3:])
print(cities[5:])







