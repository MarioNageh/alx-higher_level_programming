#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
console.log(list.map((n, i) => n * i));
#!/usr/bin/node
const dict = require('./101-data').dict;
const myNewDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (myNewDict[value] === undefined) {
    myNewDict[value] = [key];
  } else {
    myNewDict[value].push(key);
  }
}

console.log(myNewDict);
