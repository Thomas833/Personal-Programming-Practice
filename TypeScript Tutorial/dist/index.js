"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// different types of variables.
// type can be omitted and the compiler will infer
let num = 10;
let BigNum = 123_456_798;
let string = 'string';
let bool = true;
let nul_l = null;
let undef = undefined;
//let ObjectPerson = {1,"name"};
let tuple = [1, "test"]; // must be 2 elements
var ShirtSize;
(function (ShirtSize) {
    ShirtSize[ShirtSize["Small"] = 0] = "Small";
    ShirtSize[ShirtSize["Medium"] = 1] = "Medium";
    ShirtSize[ShirtSize["Large"] = 2] = "Large";
})(ShirtSize || (ShirtSize = {})); // automatically set value of small to 0 and medium to 1 and so forth
var PantSize;
(function (PantSize) {
    PantSize["Small"] = "s";
    PantSize["Medium"] = "m";
    PantSize["Large"] = "l";
})(PantSize || (PantSize = {})); // can also set to other custom value. must set all values of enum
let mySize = PantSize.Medium;
console.log(mySize);
// structures
//array elements can be any type unless specified
let NumArr = [1, 2, 3];
let arr = [1, 2, "chicken"];
// loops
NumArr.forEach;
//# sourceMappingURL=index.js.map