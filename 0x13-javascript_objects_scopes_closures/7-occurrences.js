#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Use reduce function to count occurrences of searchElement in list
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
