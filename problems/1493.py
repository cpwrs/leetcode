# Given a binary array nums, delete one element from it
# Return the size of the longest non-empty subarray containing only 1s

from typing import List

class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    max_len = 0
    count = 0
    left = 0
    
    # Window moves right pointer
    for right in range(len(nums)):
      # Check to 0s in window count
      if nums[right] == 0:
        count += 1
      # Move left pointer so theres only one 0 in window
      while (count > 1):
        if nums[left] == 0:
          count -= 1
        left += 1
      # Get length, check for new max
      length = right - left
      max_len = max(max_len, length)
        
    return max_len

# Pseudocode
# Sliding window! (window only contains one 0)
# iterate over nums
  # If the value is a 0, add one to count
  # While the count > k
    # Move left and adjust count
  # Get length of window
    # This is right - left + 1 - 1 because we are removing the 0
    # So just right - left
