#!/usr/bin/node
function multiC () {
  if (parseInt(process.argv[2])) {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      if (parseInt(process.argv[2]) <= 0) {
        break;
      } else {
        console.log('C is fun');
      }
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
multiC.call();
