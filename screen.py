import time
from ball import Ball
from paddle import Paddle
from unbreakable import Unbreakable
from normal import Normal
from colorama import init, Fore, Style
import numpy as np
from random import random, randint
from exploding import Exploding


class Screen:

    def __init__(self, reduce_life):
        self.__screen = []
        self.__length = 61
        self.__width = 31
        ball_position = randint(0, 7)
        ball_col = int(self.__length / 2) + ball_position - 2
        ball_row = self.__width - 4
        self.__balls = [Ball(ball_row, ball_col, 0, 1, True)]
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
                if(i == 5 and j > 9 and j < 21):
                    bricks.append(Exploding(i, j, False))
                    continue
                num = random()
                num2 = random()
                if(num2 < 0.3):
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
        ball_position = randint(0, 7)
        ball_col = int(self.__length / 2) + ball_position - 2
        ball_row = self.__width - 4
        self.__balls = [Ball(ball_row, ball_col, 0, 1, True)]
        self.__paddle = Paddle(self.__length, self.__width)
        self.__power_ups = []

    def __set_boundary(self):
        for i in range(0, len(self.__screen)):
            for j in range(0, len(self.__screen[i])):
                if(i == 0 or j == 0 or i == self.__width - 1 or j == self.__length - 1):
                    self.__screen[i][j] = '.'

    def __set_balls(self):
        total = 0
        for ball in self.__balls:
            if(not ball.is_present()):
                continue
            row, column, self.__bricks, value, power_up = ball.get_ball(self.__length, self.__width, self.__paddle.get_row(
            ), self.__paddle.get_left_end(), self.__paddle.get_length(), self.__bricks)
            total += value
            if(power_up != None):
                self.__power_ups.append(power_up)
            self.__screen[row][column] = '*'
        return total

    def paddle_move(self, ch):

        chosen_ball = None
        for ball in self.__balls:
            if(ball.is_start()):
                chosen_ball = ball
                break

        if(chosen_ball == None):
            for ball in self.__balls:
                if(ball.is_present()):
                    self.__paddle.move(self.__length, ball.is_start(),
                                       ch, ball.move, ball.set_start)
                    break
        else:
            self.__paddle.move(self.__length, chosen_ball.is_start(),
                               ch, chosen_ball.move, chosen_ball.set_start)

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
                    type = list(dict.keys())[0]
                    if type == "length":
                        self.__paddle.change_length(dict["length"])
                    elif type == "multiply":
                        new_balls = []
                        for ball in self.__balls:
                            if(not ball.is_present()):
                                continue
                            row, column, xv, yv = ball.get_values()
                            new_balls.append(
                                Ball(row, column, xv, -yv, False))
                        self.__balls += new_balls
                    elif type == "fast":
                        for ball in self.__balls:
                            ball.change_yv(1)
                    elif type == "through":
                        for ball in self.__balls:
                            ball.set_through(True)
                    elif type == "grab":
                        for ball in self.__balls:
                            ball.set_grab(True)
            else:
                if(int(time.time() - power_up.get_start_time()) > 5):
                    dict = power_up.reverse()
                    type = list(dict.keys())[0]
                    if type == "length":
                        self.__paddle.change_length(dict["length"])
                    elif type == "multiply":
                        flag = False
                        for j in range(0, len(self.__balls)):
                            ball = self.__balls[j]
                            if(not ball.is_present()):
                                continue
                            if(not flag):
                                flag = True
                            else:
                                self.__balls[j].finish()
                    elif type == "fast":
                        for ball in self.__balls:
                            ball.change_yv(-1)
                    elif type == "through":
                        for ball in self.__balls:
                            ball.set_through(False)
                    elif type == "grab":
                        for ball in self.__balls:
                            ball.set_grab(False)

    def __check_life(self):

        for ball in self.__balls:
            if(ball.is_present() == True):
                return True
        return False

    def print_screen(self, start_time, score, lives, game_over):
        flag = False
        for brick in self.__bricks:
            if(brick.is_present() == True):
                flag = True

        if(not flag):
            game_over()
        if(not self.__check_life()):
            self.__reduce_life()
            return 0

        time_played = int(time.time() - start_time)
        for i in range(0, len(self.__screen)):
            for j in range(0, len(self.__screen[i])):
                self.__screen[i][j] = ' '
        self.__set_boundary()
        self.__set_bricks()
        self.__set_paddle()
        value = self.__set_balls()
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
