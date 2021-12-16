import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):  # interpreter-friendly
        # Card('2', 'Diamonds')
        return f"Card('{self.rank}', '{self.suit}')"

    #  .toString
    def __str__(self):  # eyeball-friendly
        return f"{self.rank}-{self.suit}"


class CardDeck:  # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    @property
    def cards(self):
        return self._cards

    def get_dealer(self):  # getter method
        return self._dealer

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a str")

    def __len__(self):  # implements len()
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}:{self.dealer},{len(self)}"

