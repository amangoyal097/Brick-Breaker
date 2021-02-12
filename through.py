from power_up import Power_Up


class Through(Power_Up):

    def __init__(self, x, y):
        super().__init__(x, y, 'T')

    def execute(self):
        return {"through": 1}

    def reverse(self):
        self.finish()
        return {"through": 0}
