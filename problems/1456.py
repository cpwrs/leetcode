# 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the 
# maximum number of vowel letters in any substring of s with length k.

class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    if len(s) == 0: return 0
    # Apply is_vowel boolean mask
    vowels = "aeiou"
    is_vowel = [l in vowels for l in s]

    # Find first k group sum
    sumVow = sum(is_vowel[:k])
    # Set to max
    maxVow = sumVow

    # Do a loop for each remanining element
    for i in range(k, len(s)):
      # Add new element is_vowel, remove last one
      # "Slide window"
      sumVow += is_vowel[i] - is_vowel[i-k]
      # Check for a new max
      maxVow = max(maxVow, sumVow)

    return maxVow

# Pseudocode
# Initialize with sum of vowels from first k group
# Set that to a max

# Do a sliding window loop
# For each new letter, add one if vowel
# Track first vowel, subtract one if it was
# Check against max sum
# End loop

# Return max
