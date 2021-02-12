from power_up import Power_Up


class Multiplier(Power_Up):

    def __init__(self, x, y):
        super().__init__(x, y, 'x')

    def execute(self):
        return {"multiply": 1}

    def reverse(self):
        self.finish()
        return {"multiply": 0}
