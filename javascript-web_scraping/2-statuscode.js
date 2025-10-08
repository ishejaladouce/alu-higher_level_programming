#!/usr/bin/node
// 2-statuscode.js
// Display the status code of a GET request using request module

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
