#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

const firstFile = fs.readFileSync(argv[2]).toString();
const secondFile = fs.readFileSync(argv[3]).toString();
fs.writeFileSync(argv[4], firstFile + secondFile);
