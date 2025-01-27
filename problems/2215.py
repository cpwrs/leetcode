# 2215. Find the Difference of Two Arrays
# Given two 0-indexed integer arrays num1 and nums 1, return a list answer of size 2 where
# Answer[0] is all in nums1 but not nums2
# Answer[1] is all in nums2 but not nums1

from typing import List

class Solution:
  def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1-set2), list(set2-set1)]
