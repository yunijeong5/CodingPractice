# Wrong Attempt
# def trap(height):
#     if len(height) <= 1:
#         return 0
    
#     l = 0
    
#     for h in height:
#         if h == 0:
#             l += 1
#         else:
#             break
    
#     r = l 
#     between = 0
#     water = 0
    
#     while l < len(height)-1:
#       for i in range(l+1, len(height)):
#           if height[i] >= height[l]:
#               r = i
#               break;
#           else:
#               between += height[i]
          
#       if r == l:
#           l += 1
#           between = 0
#           continue

#       water += min(height[l], height[r])*(r-l-1)-between
#       l = r
        
#     return water

# Brute Force: T--O(n^2), S--O(1)
# def trap(height):
#     if len(height) <= 2:
#         return 0
    
#     water = 0
    
#     for i in range(1, len(height)-1):
#         maxl = height[i-1]
#         maxr = height[i+1]
#         l = i-2
#         r = i+2
        
#         while l >= 0:
#             maxl = max(maxl, height[l])
#             l -= 1
            
#         while r <= len(height)-1:
#             maxr = max(maxr, height[r])
#             r += 1
        
        
#         temp = min(maxl, maxr) - height[i]
#         if temp > 0:
#             water += temp
        
#     return water


# Optimal Solution: T--O(n), S--O(1)
def trap(height):
  if len(height) <= 2:
    return 0

  l = maxl = maxr = water = 0
  r = len(height)-1

  while l < r:
    hl = height[l]
    hr = height[r]

    if hl <= hr:
      if hl < maxl:
        water += maxl - hl
      else:
        maxl = hl
      l += 1
    else:
      if hr < maxr:
        water += maxr - hr
      else:
        maxr = hr
      r -= 1

  return water


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))

