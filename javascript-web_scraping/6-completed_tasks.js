#!/usr/bin/node
// 6-completed_tasks.js
// Count completed tasks per user

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedCount = {};

    todos.forEach(task => {
      if (task.completed) {
        completedCount[task.userId] = (completedCount[task.userId] || 0) + 1;
      }
    });

    console.log(completedCount);
  }
});
