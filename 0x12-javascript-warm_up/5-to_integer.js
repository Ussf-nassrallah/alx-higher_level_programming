#!/usr/bin/node
// Write a script that prints My number if the first argument can be converted to an integer

const { argv } = require('process');

let num = parseInt(argv[2]);

if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}