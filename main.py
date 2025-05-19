import random

cards = []
suits = ['spades', 'clubs', 'hearts', 'diamonds']

ranks =  (
    [{"rank":str(i), "value": i} for i in range(2,11)] + 
    [{"rank": 'A', "value": 11}] + 
    [{"rank": face, "value": 10} for face in ['J', 'Q', 'K']]
)

# Appending suit, rank pairs into cards
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
        
# Shuffle cards so that the game remains fair and unkown.
def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop() # Pop a card - this mimics the act of picking a card.
        cards_dealt.append(card)
    return cards_dealt

shuffle()
# cards_dealt = deal(2)
# card = cards_dealt[0]
# rank = card[1]

# if rank == 'A':
#     value = 11
# elif rank == 'J' or rank == 'Q' or rank == 'K':
#     value = 10
# else:
#     value = rank

# rank_dict = {"rank": rank , "value": value}
# print(rank_dict["rank"], rank_dict['value'])

card = deal(1)[0]
print(card)