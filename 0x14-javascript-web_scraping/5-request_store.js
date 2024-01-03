#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const [, , url, filePath] = process.argv;

const fileStream = fs.createWriteStream(filePath);

fileStream.on('error', (err) => {
  console.error(`Error writing to file: ${err}`);
});

request(url)
  .on('error', (err) => {
    console.error(`Error making request: ${err}`);
  })
  .pipe(fileStream)
  .on('finish', () => {
    console.log(`Content from ${url} has been stored in ${filePath}`);
  });
