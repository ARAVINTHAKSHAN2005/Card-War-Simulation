#Importing Modules 
import random 

#Declaring Global Variables 
Values = {'Two':2, 'Three':3, 'Four':4, 'Five':5,'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
Suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
Ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Jack', 'Queen', 'King', 'Ace')

# Card Class
class Card():
    def __init__(self,suit,rank):
        # Suit 
        self.suit = suit 
        # Rank
        self.rank = rank 
        # Corresponding Value  
        self.value = Values[rank]
    
    #returns rank of suit if printed 
    def __str__(self):
        return self.rank + " of " + self.suit

#Deck Class
class Deck():
    #Creates an empty list to which all cards are appended to
    def __init__(self):
        self.all_cards = []
        #The double for loop creates 13 ranks for each Suit
        for suit in Suits:
            for rank in Ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                #Appends the created cards one by one to the list.
                self.all_cards.append(created_card)

    def shuffle(self):
        #Shuffles the list containing the cards
        random.shuffle(self.all_cards)
   
    def deal_one(self):
        #pops the item of a list based on the index specified
        return self.all_cards.pop()

#Player Class 
class Player():

    def __init__(self,name):

        self.name = name 
        #Empty list to which half the deck will be randomly supplied to.
        self.all_cards = []

    def remove_one(self):
        #Removes the first card in the player's deck
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type ([]):
            #List for adding multiple card obects
            self.all_cards.extend(new_cards)
        else:
            #list for Adding one card object 
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
         

# Game Setup 
 #Declaring Players 
player_one = Player('One')
player_two = Player('Two')

#Creating A New deck 
new_deck = Deck()
#Shuffling the deck
new_deck.shuffle()

#Dealing the cards to both players, and appending the cards one after the other to player_one and player_two
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
#While game_on 
game_on = True 
round_num = 0 

while game_on:
    #Keeps track of the rounds 
    round_num += 1 

    print(f"Round {round_num }")

    #Checks if either player has ran out of cards

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins !')
        game_on = False 
        break 

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins !')
        game_on = False 
        break 

    #Start a New Round 
    player_one_cards = []
    #Removes the first card belonging to player_one and adds to player_one_cards for comparing later on 
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
     #Removes the first card belonging to player_two and adds to player_two_cards for comparing later on 
    player_two_cards.append(player_two.remove_one())

    #Setting War condition to be true to check all possible cases 
    at_war = True 

    while at_war:
        #Value of Player one cards greater than Player two 
        if player_one_cards[-1].value > player_two_cards[-1].value:
            #Adding player one's as well as player two's cards to player one's deck of cards.
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False 
        #Value of Player two cards greater than Player one
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            #Adding player one's as well as player two's cards to player two's deck of cards.
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False 
        
        else:
            #This is in case War takes place, i.e both player's card values are equal
            print('War!')

            if len(player_one.all_cards) < 5:
                #Check to see if player one can draw five cards for comparring 
                print("Player one unable to declare war")
                print("Player Two Wins ")
                game_on = False 
                break

            elif len(player_two.all_cards) < 5:
                #Check to see if player two can draw five cards for comparring 
                print("Player two unable to declare war")
                print("Player One Wins ")
                game_on = False 
                break

            else:
                #Removing 5 cards from each player's deck and depending on who has won, all 10 cards will go to respective player.
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    