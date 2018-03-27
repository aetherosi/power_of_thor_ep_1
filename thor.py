class Thor:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, pos_x, pos_y):
        self.pos_x = self.pos_x + pos_x
        self.pos_y = self.pos_y + pos_y
