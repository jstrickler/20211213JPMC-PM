from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

print(knight_data['Arthur'][0])
print(knight_data['Bedevere'][2])
print()
for name, data in knight_data.items():
    print(data[0], name)
print('-' * 60)
pprint(knight_data)
