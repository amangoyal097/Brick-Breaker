class Paddle:  # Class for the Paddle

    def __init__(self, length, width):
        # Paddle constructor
        self.__length = 7
        self.__row = width - 2
        self.__left_end = int(length / 2) - 1

    def get_dimensions(self):
        # Returns the location and size of the paddle
        return self.__row, self.__left_end, self.__length

    def move(self, length, is_start, key, move, set_start):
        # Moves the paddle left or right or releases the ball
        if(key == 'd' and length >= self.__left_end + self.__length):
            self.__left_end += 2
            if(is_start):
                move(2)

        if(key == 'a' and self.__left_end > 1):
            self.__left_end -= 2
            if(is_start):
                move(-2)

        if(key == ' '):
            set_start(False)
            self.__filled = False

    def get_length(self):
        # Returns the length of the paddle
        return self.__length

    def get_left_end(self):
        # Returns the location of the left end of the paddle
        return self.__left_end

    def get_row(self):
        # Returns the row in which the paddle is there
        return self.__row

    def change_length(self, value):
        # Increases or decreases length of the paddle
        self.__length += value
        self.__length = max(self.__length, 3)
