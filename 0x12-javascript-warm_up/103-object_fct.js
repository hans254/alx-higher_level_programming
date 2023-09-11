#!/usr/bin/node
const myObjct = {
  type: 'object',
  value: 12
};
console.log(myObjct);

myObjct.incr = function () {
  this.value++;
};

myObjct.incr();
console.log(myObjct);
myObjct.incr();
console.log(myObjct);
myObjct.incr();
console.log(myObjct);

