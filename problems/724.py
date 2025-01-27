# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of the array.
# Return the leftmost pivot index

from typing import List

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    num_range = range(len(nums))
    sumLeft = [sum(nums[i+1:]) for i in num_range]
    sumRight = [sum(nums[:i]) for i in num_range] 

    for i in num_range:
      if sumLeft[i] == sumRight[i]:
        return i

    return -1

#Psuedocode
# Make sumLeft and sumRight lists
# For each index in nums
  # Return index if sumLeft[i] == sumRight[i]
# Return -1
