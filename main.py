import os
import time
import random
from time import sleep

print('Welcome to the Dice Poker!')
game_started = False

def set_timer(delay): #Setting timer in seconds
    sleep(delay)

def draw_cube():
    while not game_started:
        cd = random.randrange(1,7) #current dice
        d = 'o'
        line = '-'*5
        e = ' '*3 #empty line
        orr = ' '*2+d #one dot on the right
        oc = ' '+d+' ' #one dot at the center
        oll = d+' '*2 #one dot on the left
        ts = d+' '+d #two dots on the side
        print(line+'\n|',end='') #drawing first row
        if cd == 1: print(e,end='')
        elif cd == 2 or cd == 3: print(orr,end='')
        elif cd == 4 or cd == 5 or cd == 6: print(ts,end='')
        print('|\n|',end='')
        if cd == 1 or cd == 3 or cd == 5: print(oc,end='') #drawing second row
        elif cd == 2 or cd == 4 or cd == 6: print(e,end='')
        print('|\n|',end='')
        if cd == 1: print(e,end='') #drawing third row
        elif cd == 2 or cd == 3: print(oll,end='')
        elif cd == 4 or cd == 5 or cd == 6: print(ts,end='')
        print('|')
        print(cd)
        set_timer(1)
        os.system('cls')

draw_cube()

def start_game():
    game_started = True