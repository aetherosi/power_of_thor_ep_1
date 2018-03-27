class Player:

    def __init__(self, thor, light_of_power):
        self.thor = thor
        self.light_of_power = light_of_power

    def move(self, direction):
        if direction in "N":
            self.thor.pos_y = self.thor.pos_y - 1
        if direction in "S":
            self.thor.pos_y = self.thor.pos_y + 1
        if direction in "E":
            self.thor.pos_x = self.thor.pos_x + 1
        if direction in "W":
            self.thor.pos_x = self.thor.pos_x - 1

