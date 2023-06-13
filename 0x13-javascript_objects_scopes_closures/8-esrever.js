#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const x = list.length;
  for (let i = 0; i < x; i++) {
    newList.push(list.pop());
  }
  return newList;
};
