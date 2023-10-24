#!/usr/bin/node
// script that prints the number of movies where
// the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  let charsCount = 0;
  let moviesData;
  let movies;
  let movieChars;

  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    moviesData = JSON.parse(body);
    movies = moviesData.results;

    for (const movieIndex in movies) {
      movieChars = movies[movieIndex].characters;

      for (const charIndex in movieChars) {
        if (movieChars[charIndex].includes('18')) {
          charsCount++;
        }
      }
    }

    console.log(charsCount);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
