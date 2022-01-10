function maxArea(height) {
  // return the max area that can be held between two vertical lines
  (l = 0), (r = height.length - 1), (maxArea = 0);

  while (l < r) {
    maxArea = Math.max(maxArea, (r - l) * Math.min(height[l], height[r]));

    if (height[l] < height[r]) {
      l += 1;
    } else {
      r -= 1;
    }
  }
  return maxArea;
}

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
