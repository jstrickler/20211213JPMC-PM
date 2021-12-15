file_path = "DATA/mary.txt"
# Absolute path:
#  C:/  //...  windows
#  /...        Non-Windows (Linux, Mac, etc)
mary_in = open(file_path, "r")
#  processing
mary_in.close()

with open(file_path) as mary_in:
    for raw_line in mary_in:  # file obj is generator of lines
        line = raw_line.rstrip()  # remove \n
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()  # read entire file
    print("RAW:")
    print(repr(contents))
    print("NORMAL")
    print(contents)  # str(contents)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

start_letter = 'z'
count = 0
letter_file = f"{start_letter}_words.txt"
with open('DATA/words.txt') as words_in:
    with open(letter_file, "w") as words_out:
        for line in words_in:
            if line.startswith(start_letter):
                count += 1
                words_out.write(line)
print(f'{count} words start with {start_letter}')

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', "w") as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

# file modes
# "r"  read
# "w"  write (destroy contents)
# "w+" read+write
# "a"  append
# "x"  open if file does not exist, otherwise error

with open('DATA/presidents.txt') as pres_in:
    with open('republicans.txt', 'w') as gop_out:
        with open('democrats.txt', 'w') as dem_out:
            with open('other_parties.txt', 'w') as other_out:
                for raw_line in pres_in:
                    line = raw_line.rstrip()
                    _, lname, fname, *_, party = line.split(':')
                    pres_name = f"{fname} {lname}\n"
                    if party == 'Republican':
                        gop_out.write(pres_name)
                    elif party == 'Democratic':
                        dem_out.write(pres_name)
                    else:
                        other_out.write(pres_name)