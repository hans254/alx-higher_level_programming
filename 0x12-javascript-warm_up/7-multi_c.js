#!/usr/bin/node

let a = 0;
const number = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  while (a < process.argv[2]) {
    console.log('C is fun');
    a++;
  }
}

