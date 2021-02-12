import time
from ball import Ball
from paddle import Paddle
from unbreakable import Unbreakable
from normal import Normal
from colorama import init, Fore, Style
import numpy as np
from random import random


class Screen:

    def __init__(self, reduce_life):
        self.__screen = []
        self.__length = 41
        self.__width = 30
        self.__ball = Ball(self.__length, self.__width)
        self.__paddle = Paddle(self.__length, self.__width)
        bricks = []
        self.__power_ups = []
        self.__reduce_life = reduce_life
        for _ in range(0, self.__width):
            row = []
            for _ in range(0, self.__length):
                row.append(' ')
            self.__screen.append(row)
        self.__set_boundary()
        for i in range(3, 8, 2):
            for j in range(4, self.__length - 6, 2):
                num = random()
                num2 = random()
                if(num2 < 0.8):
                    contains_power_up = True
                else:
                    contains_power_up = False
                if(num > 0.85):
                    bricks.append(Unbreakable(i, j, contains_power_up))
                else:
                    strength = 3
                    if(i > 6):
                        strength = 1
                    elif(i > 4):
                        strength = 2
                    bricks.append(Normal(i, j, strength, contains_power_up))
        self.__bricks = np.array(bricks)

    def new_life(self):
        self.__ball = Ball(self.__length, self.__width)
        self.__paddle = Paddle(self.__length, self.__width)
        self.__power_ups = []

    def __set_boundary(self):
        for i in range(0, len(self.__screen)):
            for j in range(0, len(self.__screen[i])):
                if(i == 0 or j == 0 or i == self.__width - 1 or j == self.__length - 1):
                    self.__screen[i][j] = '.'

    def __set_ball(self, row, column):
        self.__screen[row][column] = Fore.BLUE + '*'

    def paddle_move(self, ch):
        self.__paddle.move(self.__length, self.__ball.is_start(),
                           ch, self.__ball.move, self.__ball.set_start)

    def __set_paddle(self):
        row, left_end, length = self.__paddle.get_dimensions()
        for i in range(0, length):
            self.__screen[row - 1][left_end + i - 1] = Fore.MAGENTA + '='

    def __set_bricks(self):
        for brick in self.__bricks:
            x, y, color = brick.get_values()
            if(brick.is_present()):
                self.__screen[x][y] = color + '#'

    def __add_power_up(self, power_up):
        self.__power_ups.append(power_up)

    def __set_power_ups(self):
        row, left_end, length = self.__paddle.get_dimensions()
        for power_up in self.__power_ups:
            if(not power_up.is_present()):
                continue
            if(not power_up.is_caught()):
                x, y = power_up.get_coordinates(self.__width)
                self.__screen[x][y] = power_up.symbol()
                if(x == row - 1 and y >= left_end - 1 and y <= left_end - 1 + length):
                    power_up.caught()
                    dict = power_up.execute()
                    if "length" in dict:
                        self.__paddle.change_length(dict["length"])

            else:
                if(int(time.time() - power_up.get_start_time()) > 5):
                    dict = power_up.reverse()
                    if "length" in dict:
                        self.__paddle.change_length(dict["length"])

    def print_screen(self, start_time, score, lives):
        time_played = int(time.time() - start_time)
        for i in range(0, len(self.__screen)):
            for j in range(0, len(self.__screen[i])):
                self.__screen[i][j] = ' '
        self.__set_boundary()
        self.__set_bricks()
        self.__set_paddle()
        row, column, self.__bricks, value, power_up = self.__ball.get_ball(self.__length, self.__width, self.__paddle.get_row(
        ), self.__paddle.get_left_end(), self.__paddle.get_length(), self.__reduce_life, self.__bricks)
        self.__set_ball(row, column)
        if(power_up != None):
            self.__power_ups.append(power_up)
        self.__set_power_ups()
        print("\n\n\n\n\n\n\n\n\n")
        print("time " + str(time_played))
        print("score " + str(score))
        print("Lives " + str(lives))
        for row in self.__screen:
            print("\t\t\t\t\t\t", end="")
            for point in row:
                print(point + Style.RESET_ALL, end="")
            print()
        return value

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length
