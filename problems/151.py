# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

class Solution:
  def reverseWords(self, s: str) -> str:
    # Split the string into a list every time we hit a space
    words = s.split()
    # Join words, reversed, with a space inbetween
    return ' '.join(words[::-1])
