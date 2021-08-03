#!/usr/bin/node

const argumt = process.argv.slice(2);
if (argumt.length < 1) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
