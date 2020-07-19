import unittest
import nSum

class test_n_sum(unittest.TestCase):
    def test_2_sum(self):
        test_array = [2, 7, 11, 15]
        target = 9
        k = 2
        desired_array = [[2, 7]]
        calc_array = nSum.nSum(test_array, target, k)

        #assertion of the calculated values
        self.assertEqual(desired_array, calc_array)

    def test_3_sum(self):
        test_array = [-1, 0, 1, 2, -1, -4]
        target = 0
        k = 3
        desired_array = [[-1, -1, 2], [-1, 0, 1]]
        calc_array = nSum.nSum(test_array, target, k)

        #assertion of the calculated values
        self.assertEqual(desired_array, calc_array)

    def test_4_sum(self):
        test_array = [1, 0, -1, 0, -2, 2]
        target = 0
        k = 4
        desired_array = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        calc_array = nSum.nSum(test_array, target, k)

        #assertion of the calculated values
        self.assertEqual(desired_array, calc_array)

    # def test_5_sum(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
