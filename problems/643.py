# 643. Maximum Average Subarray 1
# You are given an integer array nums consisting of n elements, and an integer k
# Find a contiguous subarray whole length is equal to k that has the maximum average value and return this value.

# Technique: Sliding window

from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    # Sum of first k
    subSum = sum(nums[:k])
    maxSum = subSum
    # For each new element till the end
    for i in range(k, len(nums)):
      # Add new one to window, subtract first one 
      subSum += nums[i] - nums[i - k]
      # Check for new max
      maxSum = max(maxSum, subSum)

    return float(maxSum) / k

test = Solution()
print(test.findMaxAverage([1,12,-5,-6,50,3], 4))
