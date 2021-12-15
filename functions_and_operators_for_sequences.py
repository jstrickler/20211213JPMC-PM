a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("c: {}".format(c))

f = "foo"
b = "bar"
result = f + b
print("result: {}".format(result))

print('-' * 60)
banner = "Python Rocks! " * 3
print("banner: {}".format(banner))

is_prime = [True] * 10
print(is_prime)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits))

#  e1 > e2
print(len(nums), min(nums), max(nums), sum(nums))
print(sorted(nums))
print("fruits: {}\n".format(fruits))

rfruits = reversed(fruits)
print("rfruits: {}".format(rfruits))
for fruit in rfruits:
    print(fruit)
print('-' * 60)

for i, fruit in enumerate(fruits):
    print(i, fruit)
print('-' * 60)

print(list(enumerate(fruits)), '\n')
print()

efruits = enumerate(fruits)
print(efruits)
for i, fruit in efruits:
    print(i, fruit)
print()
print("Second loop:")
for i, fruit in efruits:
    print(i, fruit)
print()
