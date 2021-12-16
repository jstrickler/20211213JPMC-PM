mary_countries = ['Burkina Faso', 'Japan', 'Uruguay', 'Nepal',
          'Italy', 'Botswana', 'Spain', 'Estonia', 'Germany', 'Canada']

sue_countries = ['Japan', 'Uruguay', 'Germany', 'Canada', 'Japan',
                 'Bolivia', 'Botswana', 'Japan', 'Australia',
                 'Nepal']

empty = set()
mary = set(mary_countries)
sue = set(sue_countries)
sue.add('Argentina')

print("Common:", mary & sue)  # intersection
print("Not common:", mary ^ sue)  # xOR
print("Both:", mary | sue)  # union
print("Just Mary:", mary - sue)
print("Just Sue:", sue - mary)
