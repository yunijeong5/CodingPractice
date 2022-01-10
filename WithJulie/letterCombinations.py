"""
Given some number string, return all the letter combinations by pressing that sequece.
Assume that we can select any letter of that number in one click.
"""
def letterCombinations(numStr):
  numCharMap = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
  result = []

  def build_recur(i, curStr):
    if len(curStr) == len(numStr):
      return result.append(curStr)

    for char in numCharMap[numStr[i]]:
      build_recur(i+1, curStr+char)

  if numStr:
    build_recur(0, "")

  return result
