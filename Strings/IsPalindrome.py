def isPalindrome(s):
  s = ''.join(filter(str.isalnum, s)).lower()
  l = 0
  r = len(s)-1

  while l < r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1

  return True

class Solution: # Interesting discussion solution
  def isPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
      a, b = s[i].lower(), s[j].lower()
      if a.isalnum() and b.isalnum():
        if a != b: return False
        else:
          i, j = i + 1, j - 1
          continue
      i, j = i + (not a.isalnum()), j - (not b.isalnum())
    return True