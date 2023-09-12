#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  const n = list.length;
  let count = 0;

  for (let index = 0; index < n; index++) {
    if (list[index] === searchElement) {
      count++;
    }
  }

  return count;
}