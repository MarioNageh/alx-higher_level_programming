#!/usr/bin/node
const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);
const addTwo = (a, b) => a + b;
if (Number.isNaN(num1) || Number.isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(addTwo(num1, num2));
}
