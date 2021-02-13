from brick import Brick
from colorama import Fore


class Exploding(Brick):
    def __init__(self, x, y, contains_power_up):
        super().__init__(x, y, contains_power_up)
        self.__color = Fore.BLUE
        self._is_exploding = True

    def get_values(self):
        return self._x, self._y, self.__color
