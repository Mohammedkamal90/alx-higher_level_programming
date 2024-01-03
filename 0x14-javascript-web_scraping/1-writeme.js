#!/usr/bin/node

const fs = require('fs');

const [, , filePath, content] = process.argv;

fs.writeFile(filePath, content, (error) => {
  if (error) {
    console.error(error);
  }
});
