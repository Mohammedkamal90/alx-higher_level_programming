// 101-sorted.js

#!/usr/bin/node

const inputDict = require('./101-data').dict;

const outputDict = {};

// iterate over keys of input dictionary
for (const userId in inputDict) {
  // get number of occurrences for current user id
  const occurrences = inputDict[userId];

  // if occurrences is not a key in output dictionary, initialize it as empty array
  if (!outputDict[occurrences]) {
    outputDict[occurrences] = [];
  }

  // add current user id to list of user ids for corresponding occurrences
  outputDict[occurrences].push(userId);
}

console.log(outputDict);

