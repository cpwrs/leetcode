from typing import List

class Solution:
  def compress(self, chars: List[str]) -> int:
    # Empty list
    if len(chars) == 0: return 0

    group = 0 # Start index of current group of repeating chars
    length = 1 # Length of the current group
    i = 1 # Start loop at second char

    # We have to run once more than len(chars)
    while i <= len(chars):
      # If char is same as current group 
      if i < len(chars) and chars[i] == chars[group]:
        # Add to group length
        length += 1
      else: 
        # If it's a new char and the last group had length > 1
        if length > 1:
          # Remove all but the first char in the group
          # Append the length
          length_chars = list(str(length))
          extras = chars[group+1:i]
          chars[group+1:i] = length_chars
          # Fix our index based on how many we removed
          i = i - len(extras) + len(length_chars)
        # Reset the group index and length
        group = i
        length = 1
      i += 1

    return len(chars)
