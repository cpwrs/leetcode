# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end 
# of the merged string. Return the merged string.

class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    # Find shortest of the two
    l = min(len(word1), len(word2))
    out = ""
    
    # Add one letter from each till the shortest runs out
    for i in range(l):
      out += word1[i]
      out += word2[i]

    # Add the rest of the letters from the longest
    out += word1[l:]
    out += word2[l:]

    return out
