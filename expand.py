from power_up import Power_Up


class Expand(Power_Up):

    def __init__(self, x, y):
        super().__init__(x, y)

    def execute(self):
        return {"length": 2}

    def reverse(self):
        self.finish()
        return {"length": -2}
