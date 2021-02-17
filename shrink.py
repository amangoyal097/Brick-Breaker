from power_up import Power_Up


class Shrink(Power_Up):  # class for the Shrink Paddle Power Up

    def __init__(self, x, y):  # constructor for the class
        super().__init__(x, y, '-')

    def execute(self):  # execute the power up
        return {"length": -2}

    def reverse(self):  # reverse the effects of the power up
        self.finish()
        return {"length": +2}
