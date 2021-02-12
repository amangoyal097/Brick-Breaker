class Paddle:

    def __init__(self, length, width):
        self.__length = 7
        self.__row = width - 2
        self.__left_end = int(length / 2) - 1

    def get_dimensions(self):
        return self.__row, self.__left_end, self.__length

    def move(self, length, is_start, key, move, set_start):
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

    def get_length(self):
        return self.__length

    def get_left_end(self):
        return self.__left_end

    def get_row(self):
        return self.__row

    def change_length(self, value):
        self.__length += value
        self.__length = max(self.__length, 3)
