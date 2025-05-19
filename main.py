import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self): # this method is used to define the string representation of an object when it's printed or converted
        #to a string using str()
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']

        # Dictionary containing rank and corresponding value.
        ranks =  (
            [{"rank":str(i), "value": i} for i in range(2,11)] + 
            [{"rank": 'A', "value": 11}] + 
            [{"rank": face, "value": 10} for face in ['J', 'Q', 'K']]
        )

        # Appending suit, rank pairs into cards
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))
            
    # Shuffle cards so that the game remains fair and unkown.
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop() # Pop a card - this mimics the act of picking a card.
                cards_dealt.append(card)
        return cards_dealt


class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer    
        
    def add_card(self, card_list):
        self.cards.extend(card_list)
    # There will be a two player - Human and Program controlled dealer.

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
            
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21 
    
    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack(): 
                print("hidden")

            else:
                print(card)

        if not self.dealer:
            print("Value", self.get_value())
        print()

# class makes code go modular, we can create different objects of the class allowing different instances of the same
# class along with each object comes new set of data and functions. We will use classes to model three parts of the game
# a card, a deck, and a hand.

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <=0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number. ")  

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer = True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""

            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit'  or 'Stand' ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' or (H/S)").lower()
                    print()
                
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value() 
            dealer_hand_value = dealer_hand.get_value() 

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards = True)

            if self.check_winner(player_hand, dealer_hand):
                continue
            print("Final Results")
            print(f"Your Hand: {player_hand_value}")
            print(f"Dealer's Hand: {dealer_hand_value}")

            self.check_winner(player_hand, dealer_hand, True)
        print("\nThanks for playing!")


    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins!")
                return True
            
            elif dealer_hand.get_value() > 21:
                print("Dealer busted, You win !")
                return True

            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack! Tie!")
                return True

            elif player_hand.is_blackjack():
                print("You have a blackjack. You Win!")
                return True

            elif dealer_hand.is_blackjack():
                print("Dealer has a blackjack! Dealer wins")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")

            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie!")

            else:
                print("Dealer wins! ")
            return True
        return False
g = Game()
g.play()