# 238: Product of Array Expect Self
# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i]. 

class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    # We will calculate prefix and suffix products
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    
    for i in range(1, n):
      prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
      suffix[i] = suffix[i + 1] * nums[i + 1]

    return [prefix[i] * suffix[i] for i in range(n)]
