import os
import time
from screen import Screen


class Player():  # class for the player playing the game

    def __init__(self):  # constructor for the class
        self.__in_game = True
        self.__start_time = time.time()
        self.__score = 0
        self.__lives = 2
        self.__scr = Screen(self.reduce_life)

    def print_screen(self):  # print the screen and set the score
        self.__score += self.__scr.print_screen(self.__start_time,
                                                self.__score, self.__lives, self.game_over)

    def paddle_input(self, ch):  # pass the input to the paddle
        self.__scr.paddle_move(ch)

    def game_over(self):  # Game over for the player
        self.__in_game = 0

    def reduce_life(self):  # decrease a life of the player if present
        if(self.__lives == 0):
            self.game_over()
        else:
            self.__lives -= 1
            os.system('clear')
            self.__scr.new_life()
            print(str(self.__lives) + ' lives remaining')
            time.sleep(2)

    def set_score(self, value):  # increase the player score
        self.__score += value

    def get_values(self):  # get player stats
        return self.__start_time, self.__score

    def get_lives(self):  # get player lives
        return self.__lives

    def in_game(self):  # if player is still in game
        return self.__in_game
