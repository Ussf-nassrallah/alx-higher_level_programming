#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value
const arr = [];
exports.logMe = function (item) {
  arr.push(item);
  const itemIdx = arr.indexOf(item);
  console.log(`${itemIdx}: ${item}`);
};
