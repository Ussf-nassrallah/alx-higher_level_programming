#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const req = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';

req(`${url}/${movieId}`, function (err, res, body) {
  let movieData;
  if (err) {
    console.log(err);
  } else {
    movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
