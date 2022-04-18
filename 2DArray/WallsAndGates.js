/**
 * Given a 2D array containing -1's (walls), 0's (gates) and INF's (empty room),
 * Fill each empty room with the number of steps to the nearest gate.
 *
 * If it is impossible to reach a gate, leave INF as the value.
 *
 */
var wallsAndGates = function (grid) {
  const isInGrid = function (r, c) {
    return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
  };
  const directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];
  let queue = [];

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == 0) {
        queue.push([i, j]);
      }
    }
  }

  if (queue.length == 0) {
    // no gate
    return grid;
  }

  let distance = 0;
  while (queue.length) {
    let level_count = queue.length;

    while (level_count) {
      let cur = queue.shift();
      let r = cur[0];
      let c = cur[1];
      level_count--;
      grid[r][c] = Math.min(distance, grid[r][c]);

      for (dir of directions) {
        let row = r + dir[0];
        let col = c + dir[1];

        if (isInGrid(row, col) && grid[row][col] > 0) {
          if (grid[row][col] > distance) {
            queue.push([row, col]);
          }
        }
      }
    }
    distance++;
  }

  return grid;
};

var wallsAndGatesDFS = function (grid) {
  const isInGrid = function (r, c) {
    return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
  };
  const directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];

  //for ()
};

const grid1 = [
  [Infinity, -1, 0, Infinity],
  [Infinity, Infinity, Infinity, -1],
  [Infinity, -1, Infinity, -1],
  [0, -1, Infinity, Infinity],
];

const grid2 = [[0, Infinity, Infinity, -1, Infinity, -1, Infinity, 0]];

console.log(wallsAndGates(grid1));
console.log(wallsAndGates(grid2));
