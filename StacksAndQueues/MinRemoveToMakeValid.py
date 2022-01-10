# 
def minRemoveParen(s):
  result = list(s)
  left_paren = []

  for i in range(len(result)):
    char = result[i]

    if char == '(':
      left_paren.append(i)
    elif char == ')':
      if left_paren:
        left_paren.pop()
      else:
        result[i] = ''
  
  for i in left_paren:
    result[i] = ''

  return ''.join(result)