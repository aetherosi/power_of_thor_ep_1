import unittest

from light_of_power import LightOfPower
from game import Game
from thor import Thor


class GameTestCase(unittest.TestCase):

    def test_should_initialize_game_with_light_of_power_and_thor(self):
        thor = Thor(10, 20)
        light_of_power = LightOfPower(15, 2)

        self.game = Game(thor, light_of_power)

        self.assertEqual(thor, self.game.thor)
        self.assertEqual(light_of_power, self.game.light_of_power)

    def test_should_increase_thors_position_in_x_when_heading_east(self):
        pos_x, pos_y, expected_pos_x = 4, 10, 5
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        self.game.move("E")

        self.assertEqual(expected_pos_x, self.game.thor.pos_x)

    def test_should_decrease_thors_position_in_x_when_heading_west(self):
        pos_x, pos_y, expected_pos_x = 4, 10, 3
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        self.game.move("W")

        self.assertEqual(expected_pos_x, self.game.thor.pos_x)

    def test_should_increase_thors_position_in_y_when_heading_north(self):
        pos_x, pos_y, expected_pos_y = 4, 10, 9
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        self.game.move("N")

        self.assertEqual(expected_pos_y, self.game.thor.pos_y)

    def test_should_decrease_thors_position_in_y_when_heading_south(self):
        pos_x, pos_y, expected_pos_y = 4, 10, 11
        light_of_power = LightOfPower(15, 2)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        self.game.move("S")

        self.assertEqual(expected_pos_y, self.game.thor.pos_y)

    def test_should_pick_east_when_light_of_power_is_ahead_and_aligned_horizontally_with_thor(self):
        pos_x, pos_y, expected_direction = 4, 0, "E"
        light_of_power = LightOfPower(6, 0)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        computed_move = self.game.compute_move()

        self.assertEqual(expected_direction, computed_move)

    def test_should_pick_west_when_light_of_power_is_behind_and_aligned_horizontally_with_thor(self):
        pos_x, pos_y, expected_direction = 10, 0, "W"
        light_of_power = LightOfPower(6, 0)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        computed_move = self.game.compute_move()

        self.assertEqual(expected_direction, computed_move)

    def test_should_pick_north_when_light_of_power_is_above_and_aligned_vertically_with_thor(self):
        pos_x, pos_y, expected_direction = 6, 25, "N"
        light_of_power = LightOfPower(6, 10)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        computed_move = self.game.compute_move()

        self.assertEqual(expected_direction, computed_move)

    def test_should_pick_south_when_light_of_power_is_below_and_aligned_vertically_with_thor(self):
        pos_x, pos_y, expected_direction = 6, 30, "S"
        light_of_power = LightOfPower(6, 40)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        computed_move = self.game.compute_move()

        self.assertEqual(expected_direction, computed_move)

    def test_should_pick_south_east_when_light_of_power_is_below_and_diagonally_aligned_to_the_right_with_thor(self):
        pos_x, pos_y, expected_direction = 5, 1, "SE"
        light_of_power = LightOfPower(13, 5)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        computed_move = self.game.compute_move()

        self.assertEqual(expected_direction, computed_move)

    def test_should_pick_north_west_when_light_of_power_is_above_and_diagonally_aligned_to_the_left_with_thor(self):
        pos_x, pos_y, expected_direction = 15, 15, "NW"
        light_of_power = LightOfPower(7, 7)
        self.thor = Thor(pos_x, pos_y)
        self.game = Game(self.thor, light_of_power)

        computed_move = self.game.compute_move()

        self.assertEqual(expected_direction, computed_move)

# END GameTestCase

if __name__ == "__main__":
    unittest.main()
#  ENDIF
