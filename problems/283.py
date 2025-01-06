# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    # Pop every 0 in nums, count how many we find
    zeros = 0
    i = 0
    while i < len(nums):
      if nums[i] == 0:
        zeros += 1
        nums.pop(i)
      else:
        i += 1

    # Append the zeros we counted to the end
    nums.extend([0] * zeros)
