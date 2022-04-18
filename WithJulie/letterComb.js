function letterCombinationIter(digits) {
  if (!digits.length) return [];

  const numCharMap = { 2: ["a", "b", "c"] };

  let lastdigitcomb = [""];

  for (let i = 0; i < digits.length; i++) {
    let newcomb = [];

    for (let x = 0; x < lastdigitcomb.length; x++) {
      for (let letter of numCharMap[digits[i]]) {
        newcomb.push(lastdigitcomb[x].concat(letter));
      }
    }

    if (i == digits.length - 1) {
      return newcomb;
    }

    lastdigitcomb = newcomb;
  }
}
