import time


class Power_Up:  # parent class for the Power Ups

    def __init__(self, x, y, symbol):  # constructor for the power ups
        self.__x = x
        self.__y = y
        self.__start_time = None
        self.__is_present = True
        self.__caught = False
        self.__symbol = symbol
        self.__last_change = time.time()

    def get_coordinates(self, width):  # return the location of the power up
        if(int((time.time() - self.__last_change) / 0.1) > 1):
            self.__x += 1
            self.__last_change = time.time()
        if(self.__x == width - 1):
            self.__is_present = False
        return self.__x, self.__y

    def is_present(self):  # if the power up if present and need to be displayed
        return self.__is_present

    def get_start_time(self):  # the time when the power up was caught
        return self.__start_time

    def caught(self):  # The power up is caught by the paddle
        self.__caught = True
        self.__start_time = time.time()

    def is_caught(self):  # If the power up is caught by the paddle
        return self.__caught

    def symbol(self):  # The respective symbol of the power up
        return self.__symbol

    def finish(self):  # The power up is no longer active
        self.__is_present = False

    def execute(self):  # Execute the effect of the power up
        pass

    def reverse(self):  # Reverse the effect of the power up
        pass
