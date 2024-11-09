#!/usr/bin/node

const num1 = parseFloat(process.argv[2]);
const num2 = parseFloat(process.argv[3]);

function add (a, b) {
  return (a + b);
}

if (!isNaN(num1) && !isNaN(num2)) {
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}
