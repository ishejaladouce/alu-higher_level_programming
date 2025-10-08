#!/usr/bin/node
// 1-writeme.js
// Writes a string to a file passed as argument

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
