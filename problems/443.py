# 443. String Compression
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.

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
