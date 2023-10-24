#!/usr/bin/node
// string to file name
const fs = require('fs');

if (process.argv.length > 3) {
  fs.writeFile(process.argv[2], process.argv[3], 'utf8', (error) => {
    if (error) console.log(error);
  });
}
