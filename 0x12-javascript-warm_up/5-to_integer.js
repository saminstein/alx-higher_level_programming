#!/usr/bin/node

const argv = process.argv[2];
const number = parseInt(argv);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
