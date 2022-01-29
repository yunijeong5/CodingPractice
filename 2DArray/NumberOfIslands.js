/**
 * 200. Number of Islands
 *
 *Given an m x n 2D binary grid grid which represents a map of "1"s (land) and "0"s (water),
 * return the number of islands.
 *
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally
 * or vertically. You may assume all four edges of the grid are all surrounded by water.
 *
 */

/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = function (grid) {
  if (grid.length == 0 || grid[0].length == 0) return 0;

  const directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [-1, 0],
  ]; // up, right, down, left

  const isInGrid = function (r, c) {
    return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
  };

  let island_count = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == "1") {
        island_count++;
        const queue = [[i, j]];

        while (queue.length) {
          const cur = queue.shift();
          const r = cur[0];
          const c = cur[1];
          grid[r][c] = "0";

          for (dir of directions) {
            const next_row = r + dir[0];
            const next_col = c + dir[1];

            if (
              isInGrid(next_row, next_col) &&
              grid[next_row][next_col] == "1"
            ) {
              queue.push([next_row, next_col]);
            }
          }
        }
      }
    }
  }

  return island_count;
};

/******************************************** */

const directions = [
  [-1, 0], //up
  [0, 1], //right
  [1, 0], //down
  [0, -1], //left
];

const numIslands2 = function (grid) {
  if (grid.length === 0 || grid[0].length === 0) return 0;

  let island_count = 0;

  for (let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[0].length; col++) {
      if (grid[row][col] === "1") {
        island_count++;
        grid[row][col] = "0";
        const queue = [];
        queue.push([row, col]);

        while (queue.length) {
          const cur = queue.shift();
          const r = cur[0];
          const c = cur[1];

          for (let i = 0; i < directions.length; i++) {
            const next_row = r + directions[i][0];
            const next_col = c + directions[i][1];

            if (
              next_row < 0 ||
              next_row >= grid.length ||
              next_col < 0 ||
              next_col >= grid[0].length
            ) {
              continue;
            }

            if (grid[next_row][next_col] === "1") {
              queue.push([next_row, next_col]);
              grid[next_row][next_col] = "0";
            }
          }
        }
      }
    }
  }

  return island_count;
};

const grid1 = [
  ["1", "1", "1", "0", "1"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "1", "0", "1", "0"],
  ["1", "0", "0", "0", "1"],
];

const grid2 = [
  ["1", "1", "0", "0", "1"],
  ["0", "1", "0", "1", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "1", "0", "1", "0"],
  ["1", "0", "0", "0", "1"],
];

console.log(numIslands(grid1)); // 9
console.log(numIslands2(grid2)); // 9
console.log([[]].length);
