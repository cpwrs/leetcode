# 392. Is Subsequence
# Given two string s and t, return true if s is a subsequence of t, or false otherwise.

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    # Edge case: s is emtpy
    if len(s) == 0: return True

    # s index
    s_idx = 0
    
    # t index
    for t_idx in range(len(t)):
      # If letter is next in subsequence
      if s[s_idx] == t[t_idx]:
        # Update s_idx
        s_idx += 1
        # If that's the whole string, it's a subsequence!
        if s_idx == len(s): return True

    return False
