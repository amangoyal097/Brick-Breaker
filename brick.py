from colorama import Fore


class Brick:  # Parent Brick

    def __init__(self, x, y, contains_power_up):
        # parent constructor for bricks
        self._x = x
        self._y = y
        self._is_present = True
        self._contains_power_up = contains_power_up
        self._is_exploding = False

    def get_values(self):
        pass

    def get_coordinates(self):
        # Returns the coordinates of the brick
        return self._x, self._y

    def is_present(self):
        # Returns if the brick is present or broken
        return self._is_present

    def dec_strength(self, value):
        pass

    def destroy(self):
        # Destroys the brick regardless of type and strength
        self._is_present = False

    def is_exploding(self):
        # Returns if the brick is an exploding Brick
        return self._is_exploding

    def is_unbreakable(self):
        # Returns if the brick is unbreakable
        return False
