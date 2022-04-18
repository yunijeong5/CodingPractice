/**
 *You are given an m x n grid where each cell can have one of three values:

  0 representing an empty cell,
  1 representing a fresh orange, or
  2 representing a rotten orange.
  Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

  Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


 *Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
  Output: 4 

 *Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
  Output: -1
  Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
  because rotting only happens 4-directionally.

  Input: grid = [[0,2]]
  Output: 0
  Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 */
const directions = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

const isInGrid = (grid, r, c) => {
  return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
};

var orangesRotting = function (grid) {
  let minute = 0;
  let queue = [];
  let twoExists = false;
  let oneExists = false;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == 2) {
        for (dir of directions) {
          const row = i + dir[0];
          const col = j + dir[1];

          if (isInGrid(grid, row, col) && grid[row][col] == 1) {
            queue.push([row, col]);
            grid[row][col] = 0;
            oneExists = true;
          }
        }
        twoExists = true;
      } else if (grid[i][j] == 1) {
        oneExists = true;
      }
    }
  }

  if (!twoExists) {
    // no 2. If 1 exits, -1. If no 1, all 0.
    return oneExists ? -1 : 0;
  } else {
    // 2 exists. If 1 does not exist, return 0
    if (!oneExists) return 0;
  }

  while (queue.length) {
    let pop_count = 0;
    let level_count = queue.length;
    minute++;

    while (pop_count < level_count) {
      const cur = queue.shift();
      const r = cur[0];
      const c = cur[1];
      // grid[r][c] = 0;
      pop_count++;

      for (dir of directions) {
        const row = r + dir[0];
        const col = c + dir[1];

        if (isInGrid(grid, row, col) && grid[row][col] == 1) {
          queue.push([row, col]);
          grid[row][col] = 0;
        }
      }
    }
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == 1) {
        return -1;
      }
    }
  }

  return minute;
};

////////////////////////////////////////////////

var orangesRotting2 = function (grid) {
  let minute = -1;
  let queue = [];
  let freshOrange = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == 2) {
        queue.push([i, j]);
      } else if (grid[i][j] == 1) {
        freshOrange++;
      }
    }
  }

  // all elements are 0.
  if (queue.length == 0 && freshOrange == 0) {
    return 0;
  }

  while (queue.length) {
    let level_count = queue.length;
    minute++;

    while (level_count) {
      const cur = queue.shift();
      const r = cur[0];
      const c = cur[1];
      level_count--;

      for (dir of directions) {
        const row = r + dir[0];
        const col = c + dir[1];

        if (isInGrid(grid, row, col) && grid[row][col] == 1) {
          queue.push([row, col]);
          grid[row][col] = 2;
          freshOrange--;
        }
      }
    }
  }

  // no 2: minute == -1
  // no reachable 1: minute == 0
  // if freshOrange > 0, there must be some unreachable oranges.
  return freshOrange > 0 ? -1 : minute;
};

const grid1 = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1],
]; // 4

const grid2 = [
  [2, 1, 1],
  [1, 1, 2],
]; // 1
const grid3 = [[0, 2]]; // 0
const grid4 = [
  [2, 1, 1],
  [0, 1, 1],
  [1, 0, 1],
]; // -1
const grid5 = [
  [2, 2],
  [1, 1],
  [0, 0],
  [2, 0],
];
const grid6 = [[2, 1, 2]];
const grid7 = [[1]];

// console.log(orangesRotting(grid1));
// console.log(orangesRotting(grid2));
// console.log(orangesRotting(grid3));
// console.log(orangesRotting(grid4));
// console.log(orangesRotting(grid5));
// console.log(orangesRotting(grid6));
// console.log(orangesRotting(grid7));

console.log(orangesRotting2(grid1));
console.log(orangesRotting2(grid2));
console.log(orangesRotting2(grid3));
console.log(orangesRotting2(grid4));
console.log(orangesRotting2(grid5));
console.log(orangesRotting2(grid6));
console.log(orangesRotting2(grid7));
