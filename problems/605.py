from typing import List

class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    last = 0
    count = 0
    
    for i, current in enumerate(flowerbed):
      next = 0 if i == len(flowerbed)-1 else flowerbed[i+1]
      last = 0 if i == 0 else flowerbed[i-1]

      if current == 0 and last == 0 and next == 0:
        count += 1
        flowerbed[i] = 1
    
    return count >= n
