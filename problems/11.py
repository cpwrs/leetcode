# 11. Container with Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that
# the endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the
# x -axis form a container, such that the container contains the msot water. Return the maximum.

from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    if len(height) == 0: return 0 

    # Set left and right pointers
    left = 0
    right = len(height) - 1
    max = 0
    
    # Move left or right pointer depending on which has a taller height
    while left < right:
      # Check for a new greatest area
      area = (right - left) * min(height[left], height[right])
      if area > max: max = area

      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return max
