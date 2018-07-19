### javascript目录：

使用CryptoJS实现的前端加密：
[http://www.ContentBC.com](http://www.contentbc.com)

CryptoJS下载地址：https://pan.baidu.com/s/1eH05ByIW1TUauf_r8-YmUg

#### 备注：
components目录下的所有文件都会对应一个压缩文件，比如 components/aes.js 同时会有一个 components/aes-min.js 文件。</br>

rollups目录下的所有文件都已经压缩完毕，每个文件都可以单独调用。</br>

### nodejs目录：
使用CryptoJS实现的nodejs加密。

首先使用npm安装CryptoJS：<br>
npm install crypto-js

引用：
```javascript
var CryptoJS = require("crypto-js");
```

MD5例子：
```javascript
var valueMD5 = CryptoJS.MD5('1').toString();
```

将结果输出为Base64编码：
```javascript
var auth = CryptoJS.HmacSHA1(to_sign, key).toString(CryptoJS.enc.Base64); 
var encrypted = CryptoJS.DES.encrypt(“Message”, “Secret Passphrase”); 
var decrypted = CryptoJS.DES.decrypt(encrypted, “Secret Passphrase”); 
var encrypted = CryptoJS.AES.encrypt(“Message”, “Secret Passphrase”); 
var decrypted = CryptoJS.AES.decrypt(encrypted, “Secret Passphrase”); 
var encrypted = CryptoJS.RC4.encrypt(“Message”, “Secret Passphrase”); 
var decrypted = CryptoJS.RC4.decrypt(encrypted, “Secret Passphrase”); 
```

将内容转变为二进制：
```javascript
var key = CryptoJS.enc.Hex.parse(‘000102030405060708090a0b0c0d0e0f’); 
var iv = CryptoJS.enc.Hex.parse(‘101112131415161718191a1b1c1d1e1f’); 
var encrypted = CryptoJS.AES.encrypt(“Message”, key, { iv: iv }); 
var words = CryptoJS.enc.Base64.parse(‘SGVsbG8sIFdvcmxkIQ==’); 
var base64 = CryptoJS.enc.Base64.stringify(words); 
var words = CryptoJS.enc.Latin1.parse(‘Hello, World!’); 
```

模块编码：
```javascript
var latin1 = CryptoJS.enc.Latin1.stringify(words); 
var words = CryptoJS.enc.Hex.parse(‘48656c6c6f2c20576f726c6421’); 
var hex = CryptoJS.enc.Hex.stringify(words); 
var words = CryptoJS.enc.Utf8.parse(‘好’); 
var utf8 = CryptoJS.enc.Utf8.stringify(words); 
var words = CryptoJS.enc.Utf16.parse(‘Hello, World!’); 
var utf16 = CryptoJS.enc.Utf16.stringify(words); 
var words = CryptoJS.enc.Utf16LE.parse(‘Hello, World!’); 
var utf16 = CryptoJS.enc.Utf16LE.stringify(words);
```
