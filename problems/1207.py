# 1207. Unique Number of Occurences
# Given an array of integers arr, return true if the number of occurences of each value in the array is unique otherwise false

from typing import List

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    counts = {}
    for item in arr:
      try:
        counts[item] += 1
      except KeyError:
        counts[item] = 1

    return len(set(counts.values())) == len(counts.keys())

test = Solution()
print(test.uniqueOccurrences([1,2,2,1,1,3]))
