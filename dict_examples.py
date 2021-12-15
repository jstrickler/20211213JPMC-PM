d1 = dict()  # empty dict
d2 = {'m': 9, 'c': 11, 'e': 2}
d3 = {}  # empty dict
d2['f'] = 3
d2['r'] = 29
print("d2: {}".format(d2))
d2['m'] = 13
print("d2: {}".format(d2))
print(len(d2))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['SFO'])
print(airports['OAK'])
print()

#  {"foo": [1, 2, 3], "bar": [3, 4, 5]}
# import json
# with open('whatever.json') as json_in:
#     data = json.load(json_in)
for code in 'RDU', 'MIA', 'ORD', 'MCI', 'WOMBAT', 'LAX', 'SFO':
    print(code, code in airports)
print()

for key in 'RDU', 'LAX', 'CMH':
    print(airports.get(key, "NOT FOUND"))
print()

print("airports: {}".format(airports))
print(airports.setdefault('MCO', 'Disney'))
print(airports.setdefault('CMH', 'Columbus'))
print("airports: {}".format(airports))

print(airports.items(), '\n')

for code, name in airports.items():
    print(code, name)
print('-' * 60)






