import os
from get_input import Get, input_to
from random import randint
import time
from player import Player
os.system("resize -s 37 65")
player = Player()
while(player.in_game()):
    player.print_screen()
    ch = input_to(Get())
    if(ch == 'q'):
        break
    else:
        player.paddle_input(ch)
    os.system('clear')

start_time, score = player.get_values()
time_played = int(time.time() - start_time)
print("Game Over")
print("Time played " + str(time_played))
print("Score " + str(score))
