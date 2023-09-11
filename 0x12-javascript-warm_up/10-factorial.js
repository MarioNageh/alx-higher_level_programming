#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2]);
const factorial = (n) => {
  if (n === 0 || Number.isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(size));