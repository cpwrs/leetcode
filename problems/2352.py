# 2352. Equal row and column pairs
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (r, c)
# such that row and column are equal
# A row and column are considered equal if they contain the same elements in the same order

from typing import List
from collections import Counter

class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    rows = Counter(tuple(row) for row in grid) # Lists aren't hashable
    cols = Counter(zip(*grid))

    print(rows)
    print(cols)
    
    return sum(rows[i]*cols[i] for i in rows) # Counter returns 0 instead of KeyError

# Psuedocode
# Create counts of all columns and all rows
# Find equalPairs, which is count(row) * count(col) where row = col
# Return total pairs
