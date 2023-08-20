import random

'''
	A game that 2 players compares which card of them has higher level
	If one of them has the higher-leveled card, this player will takes compared cards
	If there are 2 cards having equal level, 2 players keep compare next cards until there is higher one
'''

values = {
	'Two' : 2,
	'Three' : 3,
	'Four' : 4,
	'Five' : 5,
	'Six' : 6,
	'Seven' : 7,
	'Eight' : 8,
	'Nine' : 9,
	'Ten' : 10,
	'Jack' : 11,
	'Queen' : 12,
	'King' : 13,
	'Ace' : 14,
}
suits = ("Hearts", 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

print("==================================")

class Deck:

	def __init__(self):
		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				#Create the Card object
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)

	def shuffle(self):
		# Do not return anything, just shuffle
		random.shuffle(self.all_cards)

	def deal_one(self):
		# Change the state of the array
		return self.all_cards.pop() 

print("==================================")

class Player:

	def __init__(self, name):
		self.name = name
		self.all_cards = []

	def remove_one(self):
		return self.all_cards.pop(0)

	def add_cards(self, new_cards):
		if type(new_cards) == type([]):
			# List of nultiple Car objects
			self.all_cards.extend(new_cards)
		else:
			# For a single Card object
			self.all_cards.append(new_cards)

	def __str__(self):
		return f"Player {self.name} has {len(self.all_cards)} card(s)."

print("==================================\n")
print("============== GAME START ==============\n")

# Game setup
play_one = Player("One")
play_two = Player("Two")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
	play_one.add_cards(new_deck.deal_one())
	play_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

# while game_on
while game_on:
	round_num += 1
	print(f"Round {round_num}!")

	if len(play_one.all_cards) == 0:
		print("Player One, out of Cards! Player Two Wins!")
		game_on = False
		break
	if len(play_two.all_cards) == 0:
		print("Player Two, out of Cards! Player One Wins!")
		game_on = False
		break

	# Start a new round
	play_one_cards = []
	play_one_cards.append(play_one.remove_one())

	play_two_cards = []
	play_two_cards.append(play_two.remove_one())

	# while at_war
	at_war = True

	while at_war:
		play_one_cards_value = 0
		play_two_cards_value = 0

		for card in play_one_cards:
			play_one_cards_value += card.value

		for card in play_two_cards:
			play_two_cards_value += card.value

		if play_one_cards_value > play_two_cards_value:
			play_one.add_cards(play_one_cards)
			play_one.add_cards(play_two_cards)

			at_war = False

		elif play_one_cards_value < play_two_cards_value:
			play_two.add_cards(play_one_cards)
			play_two.add_cards(play_two_cards)

			at_war = False

		else:
			print("WAR!!!")

			if len(play_one.all_cards) < 5:
				print("Player One unable to declare war.")
				print("PLAYER TWO WINS!")
				game_on = False
				break
			elif len(play_two.all_cards) < 5:
				print("Player Two unable to declare war.")
				print("PLAYER ONE WINS!")
				game_on = False
				break
			else:
				for num in range(5):
					play_one_cards.append(play_one.remove_one())
					play_two_cards.append(play_two.remove_one())