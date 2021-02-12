from power_up import Power_Up


class Fast(Power_Up):

    def __init__(self, x, y):
        super().__init__(x, y, 'F')

    def execute(self):
        return {"fast": 1}

    def reverse(self):
        self.finish()
        return {"fast": 0}
