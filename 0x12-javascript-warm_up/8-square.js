#!/usr/bin/node
const argument = process.argv[2];

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < argument; i++) {
    let row = '';
    for (let j = 0; j < argument; j++) {
      row += 'X';
    }
    console.log(row + '');
  }
} else {
  console.log('Missing size');
}
