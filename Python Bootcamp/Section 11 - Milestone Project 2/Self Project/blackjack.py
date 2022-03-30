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
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    while True:
        try:
            player_chips.bet = int(input('Please enter how much you want to bet.\n'))
        except ValueError:
            print("Please enter a valid integer")
        else:
            if player_chips.total < player_chips.bet:
                print("Sorry, you don't have enough money.")
            else:
                print(f"You have successfully bet ${player_chips.bet}")
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        decision = input("Hit or stand? ")

        if decision.lower() == "hit":
            hit(deck, hand)
        elif decision.lower() == "stand":
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Please try again.")
            continue
        break


def show_some(player, dealer):
    print(f"Dealer's Hand: | ??? | {dealer.cards[1]}")
    print(f"Player's Hand:", *player.cards, sep=" | ")
    print(f"Player's Hand = {player.value}")


def show_all(player, dealer):
    print(f"Dealer's Hand: ", *dealer.cards, sep=" | ")
    print(f"Dealer's Hand = {dealer.value}")
    print(f"Player's Hand: ", *player.cards, sep=" | ")
    print(f"Player's Hand = {player.value}")


def player_busts():
    print("You busted!")
    player_chips.lose_bet()


def player_wins():
    print("Congratulations, you won!")
    player_chips.win_bet()


def dealer_busts():
    print("Dealer busted!")
    player_chips.win_bet()


def dealer_wins():
    print("Dealer wins!")
    player_chips.lose_bet()


def push():
    print("The dealer and you tied!")


while True:
    # Print an opening statement
    print("Blackjack!")


    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_one = Hand()
    dealer_one = Hand()
    player_one.add_card(deck.deal())
    player_one.add_card(deck.deal())
    dealer_one.add_card(deck.deal())
    dealer_one.add_card(deck.deal())


    # Set up the Player's chips
    player_chips = Chips()


    # Prompt the Player for their bet
    take_bet()

    # Show cards (but keep one dealer card hidden)
    show_some(player_one, dealer_one)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_one)

        # Show cards (but keep one dealer card hidden)
        show_some(player_one, dealer_one)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_one.value > 21:
            player_busts()
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_one.value <= 21:
        while dealer_one.value < 17:
            hit(deck, dealer_one)

    # Show all cards
        show_all(player_one, dealer_one)

        # Run different winning scenarios
        if dealer_one.value > 21:
            dealer_busts()
        elif dealer_one.value > player_one.value:
            dealer_wins()
        elif dealer_one.value < player_one.value:
            player_wins()
        elif player_one.value > 21:
            player_busts()
        elif dealer_one.value == player_one.value:
            push()

    # Inform Player of their chips total
    print(f"You currently have {player_chips.total} amount of chips.")
    # Ask to play again
    new_game = input("\nWant to try again? Y or N. ")
    if new_game.lower() == "y":
        playing = True
        continue
    elif new_game.lower() == "n":
        print("Thank you for playing!")
        playing = False
        break
