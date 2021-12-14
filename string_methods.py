actor = "Chris Hemsworth"

print(actor)
print(type(actor), len(actor))  # not actor.length() -- discuss :-)

print(actor.upper())
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))

print(actor.startswith('Chris'), actor.startswith('Liam'))
# WilLiam
print(actor)
print(actor.find('worth'), actor.find('value'))
print(actor.find('Chris'))

s = "     Let's be bad guys      "
print(s.split())

s = "one,two,three,four"
print(s.split(','))

s = "a#b#c#d#e"
print(s.split('#'))

s = "          Let's be bad guys            "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "btbbbbbbbbteebbbeeetLet's be bad guyseeeeettttttbbbbteteteb"
print("|" + s.lstrip("bte") + "|")
print("|" + s.rstrip("bte") + "|")
print("|" + s.strip("bte") + "|")
print()

s = "how now brown cow"
print(s.title())
print(s.capitalize())
print(s.upper())
print()

print(actor)
print(actor.replace('Chris', 'Liam'))
print(actor.replace('emsw', ''))

x = "abc"
y = "def"
m = x + y

x = x + y













