#!/usr/bin/node
// 4-starwars_count.js
// Prints the number of Star Wars movies where "Wedge Antilles" is present

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
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });

    console.log(count);
  }
});
