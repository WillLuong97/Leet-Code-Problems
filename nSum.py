# Given an array nums of n integers and an integer target,
# are there elements a, b, c, and d in nums such that a + b + c + d = target? 
# Find all unique quadruplets in the array which gives the sum of target.

#function to calculate the nth amount of sum in a nums
def nSum(nums, target, k):
    nums.sort()
    retStr = []
    #check if nums is empty or would it be in a valid 
    if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
        return retStr
    #k: is the number of sum 
    if (k == 2):
        return twoSum(nums, target)

    #loop throught the nums array to find the sum
    for i in range(len(nums)):
        if(nums[i-1] != nums[i] or i == 0):
            #call the function recursively until the sum is found
            for _, value in enumerate((nSum(nums[i+1:], target - nums[i], k - 1))):
                retStr.append([nums[i]] + value)
    return retStr


def twoSum(nums, target):
    retStr = []
    left = 0
    right = len(nums) - 1

    while(left < right):
        total_sum = nums[left] + nums[right]

        if total_sum > target or (right < len(nums) - 1 and nums[right] == nums[right - 1]):
            right -= 1
        elif total_sum < target or(left > 0 and nums[left] == nums[left + 1]):
            left += 1

        else: 
            retStr.append([nums[left], nums[right]])
            left += 1
            right -= 1
        
    return retStr


# def main():
#     print("***TESTING n-SUM")
#     num_of_sum = int(input("Please specify the number of sum that you want: "))
#     target = 0
#     nums = [1, 0, -1, 0, -2, 2]
#     print( nSum(nums, target, num_of_sum))
# main()


