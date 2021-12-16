from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for num in '1', '2':
            card = Card(num, 'JOKER')
            self._cards.append(card)

