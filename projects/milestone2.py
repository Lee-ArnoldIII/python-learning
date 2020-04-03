import random
'''
Establish suits, ranks, and library for all values
'''
suits = ('Hearts', 'Diamons', 'Spades', 'Clubs')
ranks = ('Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

'''
Establish card class to create a card
'''

class Card: 

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

'''
Establish deck class to create a deck of cards from the card class
'''
class Deck: 

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The cards in the deck are: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# Sample deck for testing only
# test_deck = Deck()
# print(test_deck)

'''
Establish hand class to be able to play game later.
'''
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Code below is a an internal check as needed
# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# print(test_player.value)
# for card in test_player.cards:
#     print(card)

'''
Establish chips class to allow for betting
'''
class Chips:

    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -+ self.bet

'''
Below is all functionality to play game
'''

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Place your bet'))
        except ValueError:
            print('You must enter a number')
        else:
            if chips.bet > chips.total:
                print("You don't have enough chips! Max bet can't exceed: ", chips.total)
            else:
                print('Bet Placed! Good Luck!')
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand) # hit is defined above
        elif x[0].lower == 's':
            print('Player stands. Dealer is playing.')
            playing = False
        else:
            print('Please try again')
            continue
        break

    

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand = ", player.value)

def player_busts(player, dealer, chips):
    print('Player busts')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer Busts!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer Wins!')
    chips.lose_bet()

def push(player, dealer, chips):
    print('Dealer and player tied! Push')

'''
Build the game
'''
while True:
    print('Welcome to Black Jack!')

    # create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up player's chips
    player_chips = Chips()

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # If player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand, player_chips)

    # Inform player of their chip total
    print("\nPlayer's winnings stand at:", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    if new_game[0].lower() == 'n':
        print('Thanks for playing!')
        break