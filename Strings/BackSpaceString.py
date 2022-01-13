"""
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both 
are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


# Brute Force: T => O(m+n), S => O(m+n)
def backSpaceCompare1(s, t):
  def build_result(a):
    res = []
    for char in a:
      if char != '#':
        res.append(char)
      elif res:
        res.pop()
    
    return "".join(res)

  return build_result(s) == build_result(t)


# Optimal: T => O(m+n), S => O(1)
def backSpaceCompare2(s, t):
  def update_inner(string, p):
    hash_count = 1
    p = p-1
    while hash_count > 0 and p >= 0:
      if string[p] == '#':
          hash_count += 1
      else:
          hash_count -= 1
      p -= 1
    return p
        
  def update_pointer(string, p):
    while p >= 0 and string[p] == '#':
        p = update_inner(string, p)
    return p
      
  p1 = update_pointer(s, len(s)-1)
  p2 = update_pointer(t, len(t)-1)
  
  while p1 >= 0 and p2 >= 0:
    if s[p1] != t[p2]:
        return False
    
    p1 = update_pointer(s, p1-1)
    p2 = update_pointer(t, p2-1)
          
  return p1 == p2




# Optimal: T => O(m+n), S => O(1)
from itertools import zip_longest

def backSpaceCompare(s, t):
  def build(string):
    skip = 0
    for x in reversed(string):
      if x == '#':
        skip += 1
      elif skip:
        skip -= 1
      else:
        yield x
    
  return all(x == y for x,y in zip_longest(build(s), build(t), fillvalue='_'))

print(backSpaceCompare("aaa", "a#aaa####"))
