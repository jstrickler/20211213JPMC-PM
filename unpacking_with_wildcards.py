values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)
w, *x, y, z = values
print(w, x, y, z)
w, x, *y, z = values
print(w, x, y, z)



