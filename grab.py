from power_up import Power_Up


class Grab(Power_Up):  # class for the Grab Ball Power Up
    def __init__(self, x, y):  # constructor for the class
        super().__init__(x, y, 'G')

    def execute(self):  # execute the power up
        return {"grab": 1}

    def reverse(self):  # reverse the effects of the power up
        self.finish()
        return {"grab": 0}
