#!/usr/bin/node
const callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
exports.callMeMoby = callMeMoby;