#Python program to solve the leetcode count-and-say sequence problem
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
# You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

#Function to solve the problem
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    # base case
    if n == 1:
        return '1'
    par = countAndSay(n-1)
    ans = ''
    ii = 0
    # print(par)
    while ii<len(par):
        jj = ii
        print(ii)
        while jj < len(par) and par[jj] == par[ii]:
            jj += 1
        ans += str(len(par[ii:jj])) + str(par[ii])
        ii = jj
    return ans

#main function to run the program
def main():

    test_number_1 = 1
    test_number_2 = 2
    test_number_3 = 3
    test_number_4 = 4
    test_number_5 = 5
    test_number_6 = 6

    # print(countAndSay(test_number_1))
    print(countAndSay(test_number_2))
    # print(countAndSay(test_number_3))
    # print(countAndSay(test_number_4))
    print(countAndSay(test_number_5))
    # print(countAndSay(test_number_6))

main()

