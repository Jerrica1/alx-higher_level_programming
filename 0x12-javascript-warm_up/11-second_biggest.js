#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const parsedArr = process.argv
    .splice(2, process.argv.length - 1)
    .sort(function (a, b) {
      return a - b;
    })
    .map(function (number) {
      return parseInt(number);
    });
  console.log(parsedArr.reverse()[1]);
}
