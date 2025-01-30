# 1657. Determine if Two Strings Are Close
# Two strings are considered close if you can attain from the other using the following operations.
# 1. Swap and two existing characters
# 2. Transform every occurence of one existing char into another existing char

from typing import List

def counter(word: str):
  count = {}

  for letter in word:
    try: count[letter] += 1
    except KeyError:
      count[letter] = 1

  return count

class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    # Have the have the same length
    if len(word1) != len(word2): return False

    # Have to contain the same letters
    if set(word1) != set(word2): return False
    
    # Have to have the same occurences of letters
    list1 = sorted(counter(word1).values())
    list2 = sorted(counter(word2).values())
    if list1 != list2: return False

    return True

# Psuedocode
# The strings have to have the same length you can't change it with operations
# The strings have to have the same set you cant't add new letters
# The strings have to have the same set of letter counts for operation 2
