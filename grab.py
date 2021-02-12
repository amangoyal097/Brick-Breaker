from power_up import Power_Up


class Grab(Power_Up):
    def __init__(self, x, y):
        super().__init__(x, y, 'G')

    def execute(self):
        return {"grab": 1}

    def reverse(self):
        self.finish()
        return {"grab": 0}
