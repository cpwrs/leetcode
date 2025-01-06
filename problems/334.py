# 334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

from typing import List

class Solution:
  def increasingTriplet(self, nums: List[int]):
    # Initialize a triplet of max(nums)
    largest = max(nums)
    triplet = [largest] * 3
    
    # Loop over each num
    for i in range(len(nums)):
      # Check where it fits in the triplet
      for j in range(len(triplet)):
        # If it fits in the sequence, add it!
        if nums[i] <= triplet[j]:
          triplet[j] = nums[i]
          # If it finishes the triplet, return true!
          if j == 2: return True
          # Otherwise, continue with next num
          break
  
    return False
