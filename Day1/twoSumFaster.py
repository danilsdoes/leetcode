# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution Notes

# The overall idea of this is to sort the list of numbers and then try adding numbers together from each end
# If the sum is to small you move the small iterator up and if the sum is to big you move the big iterator down.
# This is something that is much faster when dealing with a large list however it does require making a copy
# of the list requiring more space

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # copy list
        copyNums = nums.copy()

        # sort copy
        copyNums.sort()

        # Find pair of numbers
        i = 0
        j = len(copyNums) - 1
        val1 = 0
        val2 = 0
        diff = -1
        while True:
            diff = copyNums[i] + copyNums[j] - target
            # to big
            if (diff > 0):
                j += -1
            # to small
            elif (diff < 0):
                i += 1
            # Juuuuuust right
            elif(diff == 0):
                val1 = copyNums[i]
                val2 = copyNums[j]
                break

        # Find numbers location in array
        a = nums.index(val1)

        # I was running into an issue when the values were equal (i.e. 3+3 = 6) so now if values are equal 
        # it wont look at the first one found
        if (val1==val2):
            b =  nums.index(val2, a+1)
        else:
            b =  nums.index(val2)
        return[a,b]

#Test Cases

tester = Solution()

output = tester.twoSum([2,7,6,9], 9)
print ("[0, 1] ?")
print(str(output) + "\n")

output = tester.twoSum([2,7,6,9], 15)
print ("[2, 3] ?")
print(str(output) + "\n")


output = tester.twoSum([2,7], 9)
print ("[0, 1] ?")
print(str(output) + "\n")

output = tester.twoSum([2,7,6,9,8,5,4,0], 4)
print ("[6, 7] ?")
print(str(output) + "\n")


output = tester.twoSum([-2,-7,6,9], -9)
print ("[0, 1] ?")
print(str(output) + "\n")

output = tester.twoSum([-2,-7,6,9,6], 12)
print ("[2, 4] ?")
print(str(output) + "\n")

