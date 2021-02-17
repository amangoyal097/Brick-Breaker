from brick import Brick
from colorama import Fore


class Exploding(Brick):
    def __init__(self, x, y, contains_power_up):
        # constructor for the exploding brick
        super().__init__(x, y, contains_power_up)
        self.__color = Fore.BLUE
        self._is_exploding = True

    def get_values(self):
        # Return values required to print the brick
        return self._x, self._y, self.__color
