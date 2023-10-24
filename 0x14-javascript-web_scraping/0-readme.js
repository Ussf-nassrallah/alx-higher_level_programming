#!/usr/bin/node

// import fs (file system) module in Node.js to work with files
const fs = require('fs');
// The first argument is the file path
const file = process.argv[2];
// use the fs.readFile method to read the file
// The content of the file must be read in utf-8
fs.readFile(file, 'utf-8', function (data, error) {
  // If an error occurred during the reading, print the error object
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
