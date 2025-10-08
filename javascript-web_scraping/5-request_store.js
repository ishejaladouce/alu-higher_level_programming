#!/usr/bin/node
// 5-request_store.js
// Get the contents of a webpage and store it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', err => {
    if (err) {
      console.log(err);
    }
  });
});
