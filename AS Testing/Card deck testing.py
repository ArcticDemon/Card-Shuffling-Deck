import random 
from random import shuffle 








def button():
    card_deck = ["-1H","-1D","1C","1S","9S","-9H","13S","12D"]
    user_input = input("Press Enter to shuffle cards: ")
    if len(user_input)==0:
        
    
        random.shuffle(card_deck)
    print(card_deck)

    shuffler(card_deck)


def shuffler(deck):
    for x in range(len(deck)):
        
        y = deck[x]
        colour_check = (y[0])
        if colour_check == "-":
            print("red",y)
        
        else:
            print("black",y)






button()