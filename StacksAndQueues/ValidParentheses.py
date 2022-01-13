"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.

"""


def isValid(s):
  parenMap = {'}':'{', ']':'[', ')':'('}
  left = {'{', '(', '['}
  stack = ['dummy'] # to ignore emptylist[-1] error

  for p in s:
    if p in left:
      stack.append(p)
    else:
      if parenMap[p] == stack[-1]:
        stack.pop()
      else:
        return False
        
  return len(stack) == 1
