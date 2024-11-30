#!/usr/bin/node

const args = process.argv.slice(2);
let largest;
let secondLargest = null;

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(arg => parseInt(arg, 10));

  numbers.sort((a, b) => b - a);

  largest = numbers[0];
  let i;

  for (i = 1; i < numbers.length; i++) {
    if (numbers[i] < largest) {
      secondLargest = numbers[i];
      break;
    }
  }
}

if (secondLargest !== null) {
  console.log(`${secondLargest}`);
} else {
  console.log('No Second largest');
}
