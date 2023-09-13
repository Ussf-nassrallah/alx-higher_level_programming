#!/usr/bin/node
// script that imports a dictionary of occurrences
// by user id and computes a dictionary of user ids by occurrence.
const { dict } = require('./101-data');
const newObj = {};

Object.keys(dict).forEach(function (key) {
  if (newObj[dict[key]] === undefined) {
    newObj[dict[key]] = [];
  }
  newObj[dict[key]].push(key);
});

console.log(newObj);
