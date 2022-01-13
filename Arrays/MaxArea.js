/*
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
*/

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
