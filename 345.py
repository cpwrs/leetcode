class Solution:
  def reverseVowels(self, s: str) -> str:
    vowels = "aeiouAEIOU"
    vals = []
    idxs = []

    # Create dictionary of all the vowels in s and their indexes as keys
    for i, l in enumerate(s):
      if l in vowels:
        vals.append(l)
        idxs.append(i)

    vals.reverse()

    for i,v in zip(idxs, vals):
      s = s[:i] + v + s[i+1:]

    return s

test = Solution()
print(test.reverseVowels("IceCreAm"))
