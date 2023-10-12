import unittest
import Library.utils as utils


class TestUtils(unittest.TestCase):
    def test_plus(self):
        print("test_plus")
        self.assertEqual(utils.plus(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
