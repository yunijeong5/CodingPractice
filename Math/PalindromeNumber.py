"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

"""

def isPalindrome(x):
  # Special cases:
  # As discussed above, when x < 0, x is not a palindrome.
  # Also if the last digit of the number is 0, in order to be a palindrome,
  # the first digit of the number also needs to be 0.
  # Only 0 satisfy this property.
  if (x < 0 or (x % 10 == 0 and x != 0)):
    return False

  reverted = 0
  # Since we divided the number by 10, and multiplied the reversed number by 10, 
  # when the original number is less than the reversed number, it means we've processed half of the number digits.
  while x > reverted:
    reverted = reverted * 10 + x % 10
    x = x // 10

  # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
  # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
  # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
  
  return x == reverted or x == reverted // 10


print(isPalindrome(-121))
print(isPalindrome(121))
print(isPalindrome(0))
print(isPalindrome(1000001))
print(isPalindrome(10000021))



def usingString(x):
  if x < 0:
    return False
  
  num = str(x)
  l = 0
  r = len(num)-1
  
  while l < r:
    if num[l] != num[r]:
      return False
    l += 1
    r -= 1
    
  return True

# Failed attempt

# if x < 0:
#   return False


# while x >= 10:
#   last = x % 10
#   numzero = math.floor(math.log10(x))
#   first = floor(x / 10**numzero)
  
#   if last != first:
#     return False
  
#   x = (x - first*(10**numzero)) / 10
  
# return True
      
