from carddeck import CardDeck
from jokerdeck import JokerDeck
d1 = CardDeck("Nellie")
d2 = CardDeck("Andy")
print(d1, d2)
# print(d1._dealer) # NAUGHTY!!
print(d1.get_dealer())
print(d2.get_dealer())
print('-' * 60)
print(d1.dealer)

for name in 'Bob', 42.24:
    try:
        d1.dealer = name
    except TypeError as err:
        print(err)
    else:
        print(d1.dealer)
        print(d1.dealer.upper())

d1.shuffle()
print(d1.cards)
c1 = d1.draw()
c2 = d1.draw()
print(c1, c2)
print(len(d1),len(d2))

j1 = JokerDeck('Bonnie')
print(j1)
j1.shuffle()
print(j1.draw())
print(j1.cards)

