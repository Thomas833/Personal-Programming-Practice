// different types of variables.
// type can be omitted and the compiler will infer
let num: number = 10;
let BigNum = 123_456_798;
let string: string = 'string';
let bool = true;
let nul_l = null;
let undef = undefined;
//let ObjectPerson = {1,"name"};
let tuple: [number, string] = [1, "test"] // must be 2 elements
enum ShirtSize { Small, Medium, Large } // automatically set value of small to 0 and medium to 1 and so forth
const enum PantSize { Small = 's', Medium = 'm', Large = 'l' } // can also set to other custom value. must set all values of enum
let mySize = PantSize.Medium;
console.log(mySize);

// structures

//array elements can be any type unless specified
let NumArr: number[] = [1,2,3]
let arr = [1,2,"chicken"]


// loops

NumArr.forEach