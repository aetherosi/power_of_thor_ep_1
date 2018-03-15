import unittest
from thor import Thor


class ThorTestCase(unittest.TestCase):

    def test_should_initialize_thors_position(self):
        pos_x, pos_y = 4, 10
        self.thor = Thor(pos_x, pos_y)
        self.assertEqual(pos_x, self.thor.pos_x)
        self.assertEqual(pos_y, self.thor.pos_y)


# END ThorTestCase

if __name__ == "__main__":
    unittest.main()
#  ENDIF
