class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    mostCandies = max(candies)
    return [c + extraCandies >= mostCandies for c in candies]
