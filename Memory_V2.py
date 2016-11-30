# implementation of card game - Memory

# fix black bar

import simpleguitk as simplegui
import random

# Cards
DECK_OF_CARDS = range(1, 9) + range(1, 9)
random.shuffle(DECK_OF_CARDS)
CARD_CENTER = [15, 60]
exposed = [True] * 16

STATE = 0
TURNS = 0

# helper function to initialize globals
def new_game():
    global STATE, TURNS, DECK_OF_CARDS, exposed
    STATE = 0
    TURNS = 0
    label.set_text("Turns = " + str(TURNS))  
    random.shuffle(DECK_OF_CARDS)   
    exposed = [True] * 16
     
# define event handlers
def mouseclick(pos):
    global exposed, card_1, card_2, STATE, TURNS
    """ every mouse click will 'select' a card and store its range index and change 
    the state that its from 0, 1, 2, 1, 2 and so on (calculating the turn its in). Only 2 turns
    per round. Card pairs are checked in state == 2, which is the start of the 'new'
    round(prior to re-assigning card_1)
    """
    for i in range(len(DECK_OF_CARDS)):
        index = 50 * i # calculates the width position for the card area just clicked on
        if  index < pos[0] < index + 50:
            if STATE == 0:
                TURNS += 1
                STATE = 1
                card_1 = i
                exposed[card_1] = False
            elif STATE == 1 and card_1 != i:
                TURNS += 1
                STATE = 2
                card_2 = i
                exposed[card_2] = False             
            elif STATE == 2:
                if DECK_OF_CARDS[card_2] == DECK_OF_CARDS[card_1]:
                    exposed[card_1] = False
                    exposed[card_2] = False
                else:
                    exposed[card_1] = True
                    exposed[card_2] = True  
                TURNS += 1          
                STATE = 1
                card_1 = i
                exposed[i] = False
 
    turn = "Turns: %d" % TURNS  
    label.set_text(turn)
               
# cards are logically 50x100 pixels in size    
def draw(canvas):

    for i in range(len(DECK_OF_CARDS)):
        card_position = CARD_CENTER[0] + (50 * i), CARD_CENTER[1]
        if not exposed[i] == True:
            canvas.draw_text(str(DECK_OF_CARDS[i]),card_position, 45, "white")
        else:
            width = 50
            height = 100
            X_index = 50 * i
            canvas.draw_polygon([(X_index, 0),(X_index + 50, 0), (X_index + 50, 100), (X_index, 100)], 5, "orange", "blue")      


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
