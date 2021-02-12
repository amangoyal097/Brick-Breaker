from brick import Brick
from colorama import Fore
from expand import Expand
from shrink import Shrink
from multiplier import Multiplier
from fast import Fast
from through import Through
from grab import Grab
from random import choice


class Normal(Brick):

    def __init__(self, x, y, strength, contains_power_up):
        super().__init__(x, y, contains_power_up)
        self.__strength = strength
        if(strength == 3):
            self.__color = Fore.RED
        if(strength == 2):
            self.__color = Fore.YELLOW
        if(strength == 1):
            self.__color = Fore.GREEN

    def get_values(self):
        if(self.__strength == 3):
            self.__color = Fore.RED
        if(self.__strength == 2):
            self.__color = Fore.YELLOW
        if(self.__strength == 1):
            self.__color = Fore.GREEN
        return self._x, self._y, self.__color

    def dec_strength(self, value):
        power_ups = [Grab, Shrink, Multiplier, Fast, Through, Expand]
        self.__strength -= value
        if(self.__strength == 0):
            self._is_present = False
            if(self._contains_power_up):
                return choice(power_ups)(self._x, self._y)
            else:
                return None
        else:
            return None
