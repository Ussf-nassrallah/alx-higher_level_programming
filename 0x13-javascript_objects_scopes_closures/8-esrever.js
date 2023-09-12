#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  const output = [];
  let index = list.length - 1;
  while (index >= 0) {
    output.push(list[index]);
    index--;
  }
  return output;
};
