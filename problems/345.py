# 345. Reverse vowels of a string
# Given a string s, reverse only all the vowels in the string and return it.

class Solution:
  def reverseVowels(self, s: str) -> str:
    # List of vowels to check for
    vowels = "aeiouAEIOU"
    # Pair of lists for keys and values of vowels
    vals = []
    idxs = []

    # Create dictionary of all the vowels in s and their indexes as keys
    for i, l in enumerate(s):
      if l in vowels:
        vals.append(l)
        idxs.append(i)

    # Reverse the vowels but preserve the indexes
    vals.reverse()

    # Add back the values reversed
    for i,v in zip(idxs, vals):
      s = s[:i] + v + s[i+1:]

    return s
