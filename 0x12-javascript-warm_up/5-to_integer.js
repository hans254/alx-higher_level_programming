#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: '.concat(number));
}

