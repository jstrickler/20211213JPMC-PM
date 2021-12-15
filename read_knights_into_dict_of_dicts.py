from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = {
            "title": title,
            "color": color,
            "quest": quest,
            "comment": comment,
        }

print(knight_data['Arthur']['title'])
print(knight_data['Bedevere']['quest'])
print()
for name, data in knight_data.items():
    print(data['title'], name)
print('-' * 60)
pprint(knight_data)
