#!/usr/bin/node

const arrayNumber = process.argv.slice(2);
const lenghtArrayNumbers = arrayNumber.length;
if ((lenghtArrayNumbers) < 2) {
  console.log('0');
} else {
  arrayNumber.sort((a, b) => a - b);
  console.log(arrayNumber[lenghtArrayNumbers - 2]);
}
