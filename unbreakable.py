from brick import Brick
from colorama import Fore


class Unbreakable(Brick):  # Class for unbreakable Brick
    def __init__(self, x, y, contains_power_up):
        # constructor for the unbreakable brick
        super().__init__(x, y, contains_power_up)
        self.__color = Fore.CYAN

    def get_values(self):
        # Return values required to print the brick
        return self._x, self._y, self.__color

    def is_unbreakable(self):
        # Returns is the brick is unbreakable or not
        return True
