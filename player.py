import os
import time
from screen import Screen


class Player():

    def __init__(self):
        self.__in_game = True
        self.__start_time = time.time()
        self.__score = 0
        self.__lives = 2
        self.__scr = Screen(self.reduce_life)

    def print_screen(self):
        self.__score += self.__scr.print_screen(self.__start_time,
                                                self.__score, self.__lives)

    def paddle_input(self, ch):
        self.__scr.paddle_move(ch)

    def reduce_life(self):
        if(self.__lives == 0):
            self.__in_game = 0
        else:
            self.__lives -= 1
            os.system('clear')
            self.__scr.new_life()
            print(str(self.__lives) + ' lives remaining')
            time.sleep(2)

    def set_score(self, value):
        self.__score += value

    def get_values(self):
        return self.__start_time, self.__score

    def get_lives(self):
        return self.__lives

    def in_game(self):
        return self.__in_game
