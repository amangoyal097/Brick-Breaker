from power_up import Power_Up


class Through(Power_Up):  # class for the Through Ball power up

    def __init__(self, x, y):  # constructor for the class
        super().__init__(x, y, 'T')

    def execute(self):  # execute the power up
        return {"through": 1}

    def reverse(self):  # reverse the effects of the power up
        self.finish()
        return {"through": 0}
