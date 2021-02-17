from power_up import Power_Up


class Fast(Power_Up):  # class for the Fast Ball Power Up

    def __init__(self, x, y):  # constructor for the class
        super().__init__(x, y, 'F')

    def execute(self):  # execute the power up
        return {"fast": 1}

    def reverse(self):  # reverse the effects of the power up
        self.finish()
        return {"fast": 0}
