import random

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
}
suits = ("Hearts", 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + " of " + self.rank

# ================================================


class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return f"The deck has: {deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# ================================================


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card passed in
        # from the Deck.deal() --> single Card(suit, rank)
        self.cards.append(card)

        # The value of cards on the Hand
        self.value += values[card.rank]

        # rank aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        # If total value > 21 and still have an ace
        # -> Change ace value to 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# ================================================


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# ================================================


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have {chips.total}")
            else:
                break


def hit(deck, hand):

    single_card = deck.deal()  # Take a card from the deck
    hand.add_card(single_card)  # Add that card to the hand
    hand.adjust_for_ace()		# Check if the value is > 21 and has aces


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands! Dealer's Turn.")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter h or s only!")
            continue
        break


def show_some(player, dealer):

    # dealer.cards[0] -> hidden
    # dealer.cards[1] -> show

    # Show only One of the dealer's cards
    print("\n Dealer's Hand:\n", dealer.cards[1])
    print("First card hidden")

    print("-------------------------------------")

    # Show all (2 cards) of the player's hand/cards
    print("\n Player's Hand:\n", *player.cards, sep=', ')


def show_all(player, dealer):

    # Show all the dealer's cards
    print("\n Dealer's Hand:\n", *dealer.cards, sep=', ')
    # Calculate and Display avlue (J + K == 20)
    print(f"Value of Dealer's Hand is: {dealer.value}")

    print("-------------------------------------")

    # Show all the player's cards
    print("\n Player's Hand:\n", *player.cards, sep=', ')
    print(f"Value of Player's Hand is: {player_hand.value}")


def player_busts(player, dealer, chips):
    print("BUST PLAYER!!!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!!!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!!!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!!!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player Tie! PUSH!!!")


while True:
	# Opening statement and new game
    print("WELCOME TO BLACKJACK!")
    deck = Deck()
    deck.shuffle()

    # Set a player hand and it receive 2 cards
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Set a dealer hand and it receive 2 cards
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set and Receive bet from player
    player_chips = Chips()
    take_bet(player_chips)

    # Show the original states/cards of the player and the dealer
    show_some(player_hand, dealer_hand)

    # If playing 
    while playing:

    	# Ask player want to hit or stand
        hit_or_stand(deck, player_hand)
        # If choose "stand" -> stop while loop

        show_some(player_hand, dealer_hand)

        # Check if the value of cards on player's hand is over 21
        if player_hand.value > 21:
        	# Player lost the bet
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # if the value of player's cards <= 21
    if player_hand.value <= 21:

    	# Check if the value of dealer's cards < that of player's
        while dealer_hand.value < player_hand.value:
        	# Dealer must hit more cards
            hit(deck, dealer_hand)

        # Show all cards of both when the value of dealer's cards >= player's
        show_all(player_hand, dealer_hand)

        # Check if dealer's cards value > 21
        if dealer_hand.value > 21:
        	# Dealer lose the bet
            dealer_busts(player_hand, dealer_hand, player_chips)

        # Check if dealer's cards value > player's (still <= 21)
        elif dealer_hand.value > player_hand.value:
        	# Dealer wins
            dealer_wins(player_hand, dealer_hand, player_chips)

        # Check if dealer's cards value < player's (still <= 21)
        elif dealer_hand.value < player_hand.value:
        	# Player wins
            player_wins(player_hand, dealer_hand, player_chips)

        # Otherwise, TIE
        else:
            push(player_hand, dealer_hand)
    
    print(f"\nPlayer's total chips are at: {player_chips.total}")

    # Ask for a new game
    new_game = input("Would you like to play another hand? y/n ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!!!")
        break
