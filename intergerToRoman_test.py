import unittest
import integetToRoman 
class test_roman_to_integer_conversion(unittest.TestCase):
    def test_integer_to_roman_1(self):
        test_value_1 = 1
        desired_value_1 = "I"
        result = integetToRoman.integerToRoman(test_value_1)

        #assert
        self.assertEqual(result, desired_value_1)
        # self.assertEqual(result, desired_value_1)
    
    def test_integer_to_roman_3(self):
        test_value = 3
        desired_value = "III"
        result = integetToRoman.integerToRoman(test_value)

        #assert
        self.assertEqual(result, desired_value)

    def test_integer_to_roman_4(self):
        test_value = 4
        desired_value_1 = "IV"
        result = integetToRoman.integerToRoman(test_value)

        #assert
        self.assertEqual(result, desired_value_1)

    def test_integer_to_roman_9(self):
        test_value_1 = 9
        desired_value_1 = "IX"
        result = integetToRoman.integerToRoman(test_value_1)

        #assert
        self.assertEqual(result, desired_value_1)


    def test_integer_to_roman_1994(self):
        test_value_1994 = 1994
        desired_value_1994 = "MCMXCIV"
        result_1994 = integetToRoman.integerToRoman(test_value_1994)

        #assert
        self.assertEqual(result_1994, desired_value_1994)
        # self.assertEqual(result, desired_value_1)

    def test_integer_to_roman_1000(self):
        test_value = 1000
        desired_value = "M"
        result = integetToRoman.integerToRoman(test_value)

        #assert
        self.assertEqual(result, desired_value)
        # self.assertEqual(result, desired_value_1)

    def test_integer_to_roman_1250(self):
        test_value = 1250
        desired_value = "MCCL"
        result = integetToRoman.integerToRoman(test_value)

        #assert
        self.assertEqual(result, desired_value)
        # self.assertEqual(result, desired_value_1)

    def test_integer_to_roman_FAILED(self):
        test_value = 0
        desired_value = ""
        result = integetToRoman.integerToRoman(test_value)

        #assert
        self.assertEqual(result, desired_value)
        # self.assertEqual(result, desired_value_1)


    def test_integer_to_roman_58(self):
        test_value = 58
        desired_value = "LVIII"
        result = integetToRoman.integerToRoman(test_value)

        #assert
        self.assertEqual(result, desired_value)
        # self.assertEqual(result, desired_value_1)


        
 

if __name__ == "__main__":
    unittest.main()
