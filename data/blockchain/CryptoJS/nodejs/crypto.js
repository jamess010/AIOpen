// import CryptoJS from 'crypto-js/crypto-js'
var CryptoJS = require("crypto-js");

// MD5
console.log("MD5('1')="+CryptoJS.MD5('1').toString());

// SHA256
console.log("SHA256('1')="+CryptoJS.SHA256('1').toString());

// SHA512
console.log("SHA512('1')="+CryptoJS.SHA512('1').toString());

// RIPEMD160
console.log("RIPEMD160('1')="+CryptoJS.RIPEMD160('1').toString());
