import unittest

from light_of_power import LightOfPower
from player import Player
from thor import Thor


class PlayerTestCase(unittest.TestCase):

    def test_should_initialize_player_with_light_of_power_and_thor(self):
        thor = Thor(10, 20)
        light_of_power = LightOfPower(15, 2)

        self.player = Player(thor, light_of_power)

        self.assertEqual(thor, self.player.thor)
        self.assertEqual(light_of_power, self.player.light_of_power)

    def test_should_increase_thors_position_in_x_when_heading_east(self):
        pos_x, pos_y, expected_pos_x = 4, 10, 5
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.player = Player(self.thor, light_of_power)

        self.player.move("E")

        self.assertEqual(expected_pos_x, self.player.thor.pos_x)

    def test_should_decrease_thors_position_in_x_when_heading_west(self):
        pos_x, pos_y, expected_pos_x = 4, 10, 3
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.player = Player(self.thor, light_of_power)

        self.player.move("W")

        self.assertEqual(expected_pos_x, self.player.thor.pos_x)

    def test_should_increase_thors_position_in_y_when_heading_north(self):
        pos_x, pos_y, expected_pos_y = 4, 10, 9
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.player = Player(self.thor, light_of_power)

        self.player.move("N")

        self.assertEqual(expected_pos_y, self.player.thor.pos_y)

    def test_should_decrease_thors_position_in_x_when_heading_south(self):
        pos_x, pos_y, expected_pos_y = 4, 10, 11
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.player = Player(self.thor, light_of_power)

        self.player.move("S")

        self.assertEqual(expected_pos_y, self.player.thor.pos_y)


# END PlayerTestCase

if __name__ == "__main__":
    unittest.main()
#  ENDIF
