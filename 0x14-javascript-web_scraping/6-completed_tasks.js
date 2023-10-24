#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, res, body) {
  const obj = {};
  let todos;

  if (error) {
    console.log(error);
  } else if (res.statusCode === 200) {
    todos = JSON.parse(body);

    todos.forEach(function (todo) {
      if (todo.completed) {
        const userId = todo.userId;
        if (obj[userId]) {
          obj[userId]++;
        } else {
          obj[userId] = 1;
        }
      }
    });

    console.log(obj);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
