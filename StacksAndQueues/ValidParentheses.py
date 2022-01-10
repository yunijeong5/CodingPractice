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
