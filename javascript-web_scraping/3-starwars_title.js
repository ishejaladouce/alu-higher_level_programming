#!/usr/bin/node
// 3-starwars_title.js
// Prints the title of a Star Wars movie by episode number using request module

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
