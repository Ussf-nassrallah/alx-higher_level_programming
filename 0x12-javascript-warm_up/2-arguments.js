#!/usr/bin/node
// script that prints a message depending of the number of arguments passed

const { argv } = require('process');

if (argv.length > 3) {
    console.log('Arguments found');
} else if (argv.length == 3) {
    console.log('Argument found')
} else {
    console.log('No argument');
}
