#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('NaN');
} else {
  console.log(parseInt(argv[2]) + parseInt(argv[3]));
}
