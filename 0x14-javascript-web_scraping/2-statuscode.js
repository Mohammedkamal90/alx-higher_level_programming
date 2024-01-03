#!/usr/bin/node

const request = require('request');

const [, , url] = process.argv;

request.get(url).on('response', ({ statusCode }) => {
  console.log(`code: ${statusCode}`);
});
