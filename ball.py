from random import randint
import time
import numpy as np


class Ball():

    def __init__(self, length, width):
        self.__row = width - 4
        ball_position = randint(0, 7)
        self.__column = int(length / 2) + ball_position - 2
        self.__start = True
        self.__y_velocity = 1
        self.__x_velocity = 0
        self.__last_change = time.time()

    def __paddle_collision(self, row, left_end, length):
        if(self.__start == False
           and self.__row == row - 1
           and self.__column >= left_end - 1
                and self.__column <= left_end - 1 + length):
            self.__y_velocity *= -1
            self.__x_velocity += self.__column - left_end - \
                int(length / 2) + 1

    def __set_velocity(self, length, width, row, left_end, paddle_length):

        if(self.__row == 0 or self.__row == width - 1):
            self.__y_velocity *= -1

        if(self.__column == 0 or self.__column == length - 1):
            self.__x_velocity *= -1

        self.__paddle_collision(row, left_end, paddle_length)

    def __change_velocity(self, y1, x1, x2, y2):
        xv_change = False
        yv_change = False
        y = x2 - x1
        x = y2 - y1
        if(x > y):
            if(x + y < 0):
                yv_change = True
            if(x + y > 0):
                xv_change = True
        if(x < y):
            if(x + y < 0):
                xv_change = True
            if(x + y > 0):
                yv_change = True

        return xv_change, yv_change

    def __bricks_collision(self, bricks, length, width):
        mul = 1
        if(self.__x_velocity < 0):
            mul = -1
        grid = np.empty(shape=(width + 10, length + 10), dtype=object)
        for brick in bricks:
            if(brick.is_present() == False):
                continue
            x, y = brick.get_coordinates()
            grid[x][y] = brick
        start = 1
        if(self.__x_velocity == 0):
            start = 0
        x_dist = 0
        xv_change = False
        yv_change = False
        score_inc = 0
        power_up = None
        for i in range(start, abs(self.__x_velocity) + 1):
            x_dist = mul * i
            new_x = self.__row
            new_y = self.__column + x_dist
            if(grid[new_x][new_y] != None):
                x, y = new_x, new_y
                score_inc += 10
                if(grid[x - 1][y] == None or grid[x + 1][y] == None and grid[x][y - 1] != None and grid[x][y + 1] != None):
                    yv_change = True
                else:
                    xv_change, yv_change = self.__change_velocity(
                        self.__column, self.__row, x, y)
                power_up = grid[x][y].dec_strength(1)
                break
        bricks_new = []
        for row in grid:
            for point in row:
                if(point != None):
                    bricks_new.append(point)
        bricks = np.array(bricks_new)
        if(xv_change):
            self.__x_velocity *= -1
        if(yv_change):
            self.__y_velocity *= -1
        self.__column += x_dist
        return bricks, score_inc, power_up

    def get_ball(self, length, width, row, left_end, paddle_lenth, reduce_life, bricks):
        score_inc = 0
        power_up = None
        if(not self.__start and int((time.time() - self.__last_change) / 0.1) > 0):
            self.__set_velocity(length, width, row, left_end, paddle_lenth)
            self.__row -= self.__y_velocity
            bricks, score_inc, power_up = self.__bricks_collision(
                bricks, length, width)
            self.__last_change = time.time()
        if(self.__row >= width - 1):
            reduce_life()
        self.__row = max(self.__row, 0)
        self.__column = max(self.__column, 0)
        self.__column = min(self.__column, length - 1)
        return self.__row, self.__column, bricks, score_inc, power_up

    def is_start(self):
        return self.__start

    def set_start(self, start):
        self.__start = start
        self.__last_change = time.time()

    def move(self, value):
        self.__column += value
