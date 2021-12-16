#  from __future__ import braces

city = "Jacksonville"
animal = "honey badger"  # GLOBAL(ish) variable

def spam():
    city = "Phoenix"   # LOCAL variable
    print("in spam(): animal is", animal)

spam()
print("in main: animal is", animal)
print("in main: city is", city)