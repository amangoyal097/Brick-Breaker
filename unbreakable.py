from brick import Brick
from colorama import Fore


class Unbreakable(Brick):
    def __init__(self, x, y, contains_power_up):
        super().__init__(x, y, contains_power_up)
        self.__color = Fore.CYAN

    def get_values(self):
        return self._x, self._y, self.__color
