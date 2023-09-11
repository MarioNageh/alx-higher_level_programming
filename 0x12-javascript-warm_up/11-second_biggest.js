#!/usr/bin/node
const args = process.argv;
const findSecondBiggest = (args) => {
  let biggest = Number.MIN_VALUE;
  let secondBiggest = Number.MIN_VALUE;

  for (let i = 2; i < args.length; i++) {
    args[i] = parseInt(args[i]);
    if (args[i] > biggest) {
      secondBiggest = biggest;
      biggest = args[i];
    } else if (args[i] > secondBiggest && args[i] < biggest) {
      secondBiggest = args[i];
    }
  }
  return secondBiggest;
};
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(findSecondBiggest(args));
}
