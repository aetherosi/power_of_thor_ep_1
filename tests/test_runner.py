import unittest

from light_of_power import LightOfPower
from runner import Runner
from thor import Thor


class RunnerTestCase(unittest.TestCase):

    def test_should_initialize_runner_with_light_of_power_and_thor(self):
        thor = Thor(10, 20)
        light_of_power = LightOfPower(15, 2)

        self.runner = Runner(thor, light_of_power)

        self.assertEqual(thor, self.runner.thor)
        self.assertEqual(light_of_power, self.runner.light_of_power)


# END RunnerTestCase

if __name__ == "__main__":
    unittest.main()
#  ENDIF
