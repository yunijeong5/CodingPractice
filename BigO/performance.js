const arr = [1, 2, 3, 4, 5, 6, 7, 8];

function findFive(arr) {
  let t0 = performance.now();
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == 5) {
      console.log("found five!");
    }
  }
  let t1 = performance.now();
  console.log("Call to find five took "(t1 - t0) + "milliseconds.");
}

findFive(arr);
