import unittest

from light_of_power import LightOfPower


class LightOfPowerTestCase(unittest.TestCase):

    def test_should_initialize_light_of_power_position(self):
        pos_x, pos_y = 4, 10
        self.light_of_power = LightOfPower(pos_x, pos_y)
        self.assertEqual(pos_x, self.light_of_power.pos_x)
        self.assertEqual(pos_y, self.light_of_power.pos_y)


# END LightOfPowerTestCase

if __name__ == "__main__":
    unittest.main()
#  ENDIF
