#!/usr/bin/node
const data = require('./100-data').list;
const newArray = data.map((value, index) => value * index);
console.log(data);
console.log(newArray);

