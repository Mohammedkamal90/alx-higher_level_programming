#!/usr/bin/node
exports.esrever = function (list) {
  // Create new array and populate it with element in reversed order
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
