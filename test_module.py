import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(mean_var_std.calculate([0,1,2,3,4,5,6,7,8])['mean'], [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0])
    
    def test_less_than_9_values(self):
        with self.assertRaises(ValueError):
            mean_var_std.calculate([1,2,3,4,5,6,7,8])

if __name__ == "__main__":
    unittest.main()
