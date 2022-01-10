class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop() {
    const lastItem = this.data[this.length - 1];
    // delete removes a property from an object
    delete this.data[this.length - 1];
    this.length--;
    return lastItem;
  }

  delete(index) {
    const targetItem = this.data[index];
    this.shiftItems(index);
    return targetItem;
  }

  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    delete this.data[this.length - 1];
    this.length--;
  }

  length() {
    return this.length;
  }
}

const newArray = new MyArray();
newArray.push("A");
newArray.push("B");
console.log(newArray.get(1));

console.log(newArray);
