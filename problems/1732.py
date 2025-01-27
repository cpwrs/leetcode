# 1732. Find the Highest Altitude
# There's a boker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on
# point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between i and i + 1. 
# Return the highest altitude of a point.

from typing import List

class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    max_alt = 0
    alt = 0

    for i in range(len(gain)):
      alt += gain[i]
      max_alt = max(alt, max_alt)

    return max_alt

# Psuedocode
# Method: Prefix sum
# Create a list of len(gain) + 1 altitudes
# First altitude is 0
# Add gain to last altitude
# Check for a new max altitude
# Continue
