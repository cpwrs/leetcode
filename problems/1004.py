# Given a binary array nums and an integer k, return the max # of consecutive 1s in the array if you can flip at most k 0s

from typing import List

class Solution:
  def longestOnes(self, nums: List[int], k: int) -> int:
    if len(nums) == 0: return 0
    left, max_len, count = 0, 0, 0
    
    for right in range(len(nums)):
      if nums[right] == 0:
        count += 1
      while count > k:
        if nums[left] == 0:
          count -= 1
        left += 1
      max_len = max(max_len, right - left + 1) 

    return max_len
      
# Psuedocode

# For each index
  # Add one to count if the right is a 0
  # Move the left pointer until count = k
  # Get the length, compare to max
