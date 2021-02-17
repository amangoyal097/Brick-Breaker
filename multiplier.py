from power_up import Power_Up


class Multiplier(Power_Up):  # class for the Multiple Balls Power Up

    def __init__(self, x, y):  # constructor for the class
        super().__init__(x, y, 'x')

    def execute(self):  # execute the power up
        return {"multiply": 1}

    def reverse(self):  # reverse the effects of the power up
        self.finish()
        return {"multiply": 0}
