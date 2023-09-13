#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!this.checkForANumber(w) || !this.checkForANumber(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  checkForANumber (value) {
    if (isNaN(value) || value <= 0) {
      return false;
    }
  }
}
module.exports = Rectangle;
