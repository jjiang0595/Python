import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += card.__str__() + ',  '
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card]

    def adjust_for_ace(self):
        if self.value > 10:
            values['Ace'] = 1
        else:
            values['Ace'] = 11


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        self.balance = 0

    def win_bet(self):
        balance = self.total + self.bet
        return balance

    def lose_bet(self):
        balance = self.total - self.bet
        return balance


def take_bet():
    bet = input("Please enter how much you want to bet.\n")
    try:
        int(bet)
    except ValueError:
        print("Please enter a valid integer")
    else:
        print(f"You have successfully bet ${bet}")


def hit(deck,hand):
    hand.append(deck.deal())


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    decision = input("Hit or stand?")

    if decision.lower() == "hit":
        hit()
    elif decision.lower() == "stand":
        playing = False


def show_some(player, dealer):
    player_first_card = player.add_card(new_deck.deal())
    dealer_first_card = dealer.add_card(new_deck.deal())
    print(f"Player: {player_first_card}\nDealer: ?")


def show_all(player, dealer):
    player.add_card(new_deck.deal())


new_deck = Deck()
new_deck.shuffle()
player_one = Hand("One")
dealer_one = Hand("Two")

show_some(player_one, dealer_one)
