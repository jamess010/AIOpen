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


var NodeRSA = require("node-rsa");

var key = new NodeRSA({b:512});

var pubkey = key.exportKey('pkcs8-public');//导出公钥
var prikey = key.exportKey('pkcs8-private');//导出私钥
// var pubKey = new NodeRSA(pubKey,'pkcs8-public');//导入公钥
// var priKey = new NodeRSA(priKey,'pkcs8-private');//导入私钥

console.log("PriKey:"+prikey);
console.log("PubKey:"+pubkey);

var message = "www.ContentBC.com";

//var pubKey = key.exportKey('pkcs8-public');//

// 公钥加密，私钥解密，用于非对称加密（公钥加密）
pubKey = new NodeRSA(pubkey,'pkcs8-public');
var encrypted = pubKey.encrypt(message, 'base64');
console.log('公钥加密的数据',encrypted);

priKey = new NodeRSA(prikey,'pkcs8-private');
var decrypted = priKey.decrypt(encrypted, 'utf8');
console.log('私钥解密的数据',decrypted);


// 签名和验签
// 私钥签名(返回签名):
priKeySig = new NodeRSA(prikey,'pkcs8-private');
var signature = priKeySig.sign(message);
console.log('签名的数据',signature);

// 公钥验证(返回true或false):
pubKeySig = new NodeRSA(pubkey, 'pkcs8-public');
var flag = pubKeySig.verify(message, signature);
console.log("验签结果："+ flag);
