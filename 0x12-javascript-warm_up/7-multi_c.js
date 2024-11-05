#!/usr/bin/node

const x = process.argv[2];
const number = parseInt(x);

let i;
if (!isNaN(number)) {
  for (i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
