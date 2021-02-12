from colorama import Fore


class Brick:

    def __init__(self, x, y, contains_power_up):
        self._x = x
        self._y = y
        self._is_present = True
        self._contains_power_up = contains_power_up

    def get_coordinates(self):
        return self._x, self._y

    def is_present(self):
        return self._is_present

    def dec_strength(self, value):
        pass
