import os
from get_input import Get, input_to
from random import randint
import time
from player import Player
os.system("resize -s 37 65")
player = Player()  # Initalized the player playing the Game
while(player.in_game()):  # Checks if the player is still in the game
    player.print_screen()  # Prints the whole screen
    ch = input_to(Get())  # Takes input every 0.1 seconds
    if(ch == 'q' or ch == 'Q'):  # If the player presses q the game is over
        break
    else:
        # Pass the input to the paddle to move or to release the ball
        player.paddle_input(ch)
    os.system('clear')

# Game Over display
start_time, score = player.get_values()
time_played = int(time.time() - start_time)
print("Game Over")
print("Time played " + str(time_played))
print("Score " + str(score))
