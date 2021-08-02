#!/usr/bin/node
const argument = process.argv[2];

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < argument; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
