fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

#    [EXPR for VAR in ITERABLE]
f1 = [f.upper() for f in fruits]  # list comprehension
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

with open('DATA/words.txt') as words_in:
    x_words = [w.rstrip() for w in words_in if w.startswith('x')]
    print(x_words)
    print('-' * 60)

fgen = (f.upper() for f in fruits)
print(fgen)
for f in fgen:
    print(f)


