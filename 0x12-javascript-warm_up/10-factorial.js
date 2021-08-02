#!/usr/bin/node

function factorial (num) {
  if (!isNaN(parseInt(num)) && num > 0) {
    return (num * factorial(num - 1));
  } else {
    return (1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
