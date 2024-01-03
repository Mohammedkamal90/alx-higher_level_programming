#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode === 200) {
    const completedTasks = {};
    const tasks = JSON.parse(body);

    for (const task of tasks) {
      if (task.completed === true) {
        completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
      }
    }

    console.log(completedTasks);
  } else {
    console.error(`An error occurred. Status code: ${response.statusCode}`);
  }
});
