#!/usr/bin/node
// script that writes a string to a file.

// import fs (file system) module in Node.js to work with files
const fs = require('fs');
// The first argument is the file path
const file = process.argv[2];
// The second argument is the string to write
const fileContent = process.argv[3];
// use the fs.writeFile method to write in the file
// The content of the file must be written in utf-8
fs.writeFile(file, fileContent, 'utf-8', function (error) {
  if (error) {
    // If an error occurred during while writing, print the error object
    console.log(error);
  }
});
