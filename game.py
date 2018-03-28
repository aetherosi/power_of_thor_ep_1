from light_of_power import LightOfPower
from thor import Thor


class Game:

    def __init__(self, thor, light_of_power):
        self.thor = thor
        self.light_of_power = light_of_power

    def move(self, direction):
        directions = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
            'W': (-1, 0),
            'NW': (-1, -1),
            'NE': (1, -1),
            'SW': (-1, 1),
            'SE': (1, 1)
        }
        x, y = directions[direction]
        self.thor.move(x, y)

        # Another possibility : self.thor.move(*directions[direction])

    def compute_move(self):
        direction = ""
        x_delta = self.thor.pos_x - self.light_of_power.pos_x
        y_delta = self.thor.pos_y - self.light_of_power.pos_y

        if y_delta != 0:
            direction += "S" if y_delta < 0 else "N"

        if x_delta != 0:
            direction += "E" if x_delta < 0 else "W"

        return direction


def main():
    light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
    light_of_power = LightOfPower(light_x, light_y)
    thor = Thor(initial_tx, initial_ty)
    game = Game(thor, light_of_power)

    while True:
        remaining_turns = int(input())
        if remaining_turns >= 0:
            direction = game.compute_move()

            print(direction)
            game.move(direction)


if __name__ == "__main__": main()
