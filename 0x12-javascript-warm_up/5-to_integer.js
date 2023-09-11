#!/usr/bin/node
// Write a script that prints My number if the first argument can be converted to an integer

const { argv } = require('process');

if (isNaN(argv[2]) || argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argv[2]));
}
