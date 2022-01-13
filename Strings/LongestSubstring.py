"""
3. Longest Substring Without Repeating Characters

Given a string s, 
find the length of the longest substring without repeating characters.

"""

# Brute Force: Time O(n^2), Space O(n)
def lengthOfLongestSubstring1(s):
  if len(s) <= 0:
    return len(s)

  p = 0
  maxlen = 0
  seen = set()

  while p < len(s):
    for i in range(p, len(s)):
      if s[i] in seen:
        p += 1
        maxlen = max(maxlen, len(seen))
        seen = set()
        break;
      else:
        seen.add(s[i])
        maxlen = max(maxlen, len(seen))
  return maxlen


# Optimal: Time O(n), Space O(n)
def lengthOfLongestSubstring1(s):
  if len(s) <= 1:
    return len(s)

  l = r = maxlen = 0
  seen = {}

  while r < len(s):
    cur = s[r]
    if cur in seen and seen[cur] >= l:
      l = seen[cur] + 1
    
    seen[cur] = r
    maxlen = max(maxlen, r - l + 1)
    r += 1
    

  return maxlen


