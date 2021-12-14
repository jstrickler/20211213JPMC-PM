i = 0
while i < 3:
    print(i)
    i += 1
print('-' * 60)

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break  # exit loop
    if name.strip() == '':
        print("   -- please enter a name")
        continue  # go to top
    print("Welcome,", name)

