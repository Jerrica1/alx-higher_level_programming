#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  for (let i = 0; i < list.length; i++) {
    reverse[list.length - i - 1] = list[i];
  }
  return reverse;
}];
