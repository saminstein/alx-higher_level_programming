#!/usr/bin/node

const number = process.argv[2];
const size = parseInt(number);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < size; r++) {
    let row = '';
    for (let c = 0; c < size; c++) {
      row += 'X';
    }
    console.log(row);
  }
}
