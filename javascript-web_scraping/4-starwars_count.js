#!/usr/bin/node
// 4-starwars_count.js
// Count the number of movies where "Wedge Antilles" appears

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      // Count if any character URL ends with '/18/'
      if (film.characters.some(charURL => charURL.endsWith('/18/'))) {
        count++;
      }
    });

    console.log(count);
  }
});
