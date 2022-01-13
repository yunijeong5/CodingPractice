"""
680. Valid Palindrome II

Given a string s, return true 
if the s can be palindrome after deleting at most one character from it.

"""
def almostPalindrome(s: str) -> bool:
  # assume that s only consists of lowercase chars. 
  def subpalindrome(s, l, r):
      while l < r:
          if s[l] != s[r]:
              return False
          l += 1
          r -= 1
      return True
  
  l = 0
  r = len(s) - 1
  
  while l < r:
      if s[l] != s[r]:
          return subpalindrome(s, l+1, r) or subpalindrome(s, l, r-1)
      l += 1
      r -= 1
      
  return True

def almostPalindrome2(s: str) -> bool:
  # assume that s only consists of lowercase chars. 
  def subpalindrome(s, l, r):
      while l < r:
          if s[l] != s[r]:
              return False, l, r
          l += 1
          r -= 1
      return True, l, r
  
  palin, l, r = subpalindrome(s, 0, len(s)-1)
  
  if palin: # perfect palindrome
      return True
  
  # at least one of them should be palindrome
  res1, l1, r1 = subpalindrome(s, l+1, r)
  res2, l2, r2 = subpalindrome(s, l, r-1)
  
  return res1 or res2



def almostPalindrome3(s: str) -> bool:
  lp = 0              #starts at beginning of string
  rp = len(s) - 1     #starts at end of string

  while lp < rp:      #while end of string index > beginning of string index
      if s[lp] == s[rp]: #advance index, palindrome!
          lp += 1
          rp -= 1
      else:           #palindrome encountered different letter
          cand_s = s[:lp] + s[lp+1:]  #skips letter on the left pointer side ('abca' skips b)
          if is_pal(cand_s):
              return True
          cand_s = s[:rp] + s[rp+1:]  #skips letter on the right pointer side ('abca' skips c)
          if is_pal(cand_s):
              return True
          return False

  return True                              #assuming no letter differences were encountered, just return True

def is_pal(s: str) -> bool:
    revS = s[::-1]                      #reverses string
    return s == revS                    #checks if palindrome
    