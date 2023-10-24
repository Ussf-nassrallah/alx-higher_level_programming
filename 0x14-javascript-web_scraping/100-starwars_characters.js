#!/usr/bin/node
// script that prints the chars of a Star Wars movie

const req = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';

req(`${url}/${movieId}`, function (err, res, body) {
  let movieData;
  let movieChars;
  let movieChar;
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    movieData = JSON.parse(body);
    movieChars = movieData.characters;

    for (const charIndex in movieChars) {
      req(movieChars[charIndex], function (err, res, body) {
        if (err) {
          console.log(err);
        } else if (res.statusCode === 200) {
          movieChar = JSON.parse(body);
          console.log(movieChar.name);
        } else {
          console.log('code: ' + res.statusCode);
        }
      });
    }
  } else {
    console.log('code: ' + res.statusCode);
  }
});
