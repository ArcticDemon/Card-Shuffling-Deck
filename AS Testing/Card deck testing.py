import random 
from random import shuffle 


stack_1 = []
stack_2 = []
reserve_stack = []





def button():
    card_deck = ["-1H","-1D","1C","1S","9S","-9H","13S","12D"]
    print(card_deck)
    user_input = input("Press Enter to shuffle cards\nOr [q] to quit: ")
    
    if len(user_input)==0:
        
    
        random.shuffle(card_deck)
    
    else: 
        quit()
    
    stacker(card_deck)

    #colour_sort(card_deck)
   
    
    
    
    


def colour_sort(deck):
    for x in range(len(deck)):
        
        y = deck[x]
        colour_check = (y[0])
        if colour_check == "-":
            print("red",y)
        
        else:
            print("black",y)
    
    print("----------------------------")
    
    button()



def stacker(deck):
    for i in range(len(deck)):
        if i == 0 or i == 1:
            reserve_stack.append(deck[i])        
        
        elif i%2==0:
            stack_1.append(deck[i])
        else: 
            stack_2.append(deck[i])
        
    print(stack_1,"\n",stack_2, "\n", reserve_stack)    
    



def quit():
    print("Quitting")
    raise SystemExit



button()

#card_deck = ["-1H","-1D","1C","1S","9S","-9H","13S","12D"]
#stack_1 = []
#stack_2 = []
#reserve_stack = []

#for i in range(len(card_deck)):
    
    #if i == 0 or i == 1:
        #reserve_stack.append(card_deck[i])
    
    #elif i%2==0:
        #stack_1.append(card_deck[i])
    #else: 
        #stack_2.append(card_deck[i])
    
#print(stack_1, "\n", stack_2, "\n", reserve_stack)
    