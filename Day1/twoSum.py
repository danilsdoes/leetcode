# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution Notes.
# This is a rather simple first attempt where you just try every possible iteration to see if it can be done
# this does not take time complexity into account at all as it is O(n^2)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]


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

