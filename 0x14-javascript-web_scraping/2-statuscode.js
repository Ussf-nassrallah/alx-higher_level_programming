#!/usr/bin/node
// script that display the status code of a GET request.

// use request module to send a GET request.
const req = require('request');
// The first argument is the URL to request (GET)
const url = process.argv[2];

req(url, function (error, res) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
