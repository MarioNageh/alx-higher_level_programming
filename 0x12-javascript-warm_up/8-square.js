#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
