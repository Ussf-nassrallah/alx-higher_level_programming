#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (error, res, body) {
  if (error) {
    console.log(error);
  } else if (res.statusCode === 200) {
    fs.writeFile(fileName, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('code: ' + res.statusCode);
  }
});
