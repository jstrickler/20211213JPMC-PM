person = "Santa Claus"
city = "the North Pole"
value = 31.139023503

print(person, city, value)
#  str(person) + sep + str(city) + sep + str(value) + end

print("Done.")

print(person, city, value, sep="/")
print(person, city, value, sep=", ")
print(person)
print(city)
print(value)

print(person, end="=")
print(city, end="/")
print(value)

print(person, "lives at", city)
print("{} lives at {}".format(person, city))
print(f"{person} lives at {city}") # f-string
print("%s lives at %s" % (person, city))

print("Value is {}".format(value))
print(f"Value is {value}")
print("Value is {:.2f}".format(value))
print(f"Value is {value:.2f}")

big_number = 2398029302
print(f"Big number is {big_number:,d}")
print(f"Big number is {big_number:b}")

s = "abc"
bstring = s.encode()
print("bstring: {}".format(bstring))
bs = ''.join([f"{b:b}" for b in bstring])
print("bs: {}".format(bs))

