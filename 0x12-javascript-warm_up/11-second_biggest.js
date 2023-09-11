#!/usr/bin/node

const siz = process.argv.length;

if (siz <= 3) {
  console.log(0);
} else {
  const newC = process.argv.map(Number);
  newC.slice(2, siz);
  newC.sort((a, b) => a - b);
  console.log(newC[newC.length - 2]);
}

