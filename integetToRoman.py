#Python function to convert an integer into a roman numeral string
#The given integer will be between 1 and 3999
def integerToRoman(nums):
    retStr = ""
    #input number validation: 
    if(nums < 1 and nums > 3999):
        return retStr
    #create two arrays to store the interger and value of the covnersinon table
    numeric_value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_value = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    numsOfValues = 12
    #as long as the number is not 0
    while nums:
        remainder =  nums // numeric_value[numsOfValues]
        nums %= numeric_value[numsOfValues]

        while remainder:
            retStr += roman_value[numsOfValues]
            remainder -= 1
        numsOfValues -= 1

    return retStr

        

            

#Main function to test the program
def main():
    test_number_1 = 1
    test_number_1994 = 1994
    # print(integerToRoman(test_number_1))
    print(integerToRoman(test_number_1994))

main()