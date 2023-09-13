#!/usr/bin/node
const { list } = require('./100-data');
const newList = list.map((ele, index) => ele * index);

console.log(list);
console.log(newList);
