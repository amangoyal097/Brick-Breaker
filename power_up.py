import time


class Power_Up:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__start_time = None
        self.__is_present = True
        self.__caught = False
        self.__symbol = '@'
        self.__last_change = time.time()

    def get_coordinates(self, width):
        if(int((time.time() - self.__last_change) / 0.1) > 1):
            self.__x += 1
            self.__last_change = time.time()
        if(self.__x == width - 1):
            self.__is_present = False
        return self.__x, self.__y

    def is_present(self):
        return self.__is_present

    def get_start_time(self):
        return self.__start_time

    def caught(self):
        self.__caught = True
        self.__start_time = time.time()

    def is_caught(self):
        return self.__caught

    def symbol(self):
        return self.__symbol

    def finish(self):
        self.__is_present = False
