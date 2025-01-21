# 1679. Max Number of K-Sum Pairs
# You are given an integer array nums and an integer k. In one operation, you can pick two 
# numbers from the array whos sum equals k and remove them from the array.
# Return the maximimum number of operations you can perform.
from typing import List

class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    # Sort the array and make left and right pointers
    nums.sort()
    l, r = 0, len(nums) - 1

    # Count the number of operations we can perform
    ops = 0

    # While we can still move the pointers
    while l < r:
      sum = nums[l] + nums[r]
      # If the sum is k, move both pointers and add to the ops count
      if sum == k:
        ops += 1
        l += 1
        r -= 1
      # If the sum is less than k, make it bigger by moving l
      elif sum < k:
        l += 1
      # If the sum is more than k, make it smaller by moving r
      else:
        r -= 1

    return ops
