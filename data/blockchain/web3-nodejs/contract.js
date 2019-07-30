// node (web3)

// 定义 web3 库

var Web3 = require('web3');

// 链接以太网络
// truffle unbox react
web3 = new Web3( new Web3.providers.HttpProvider("http://localhost:8545") );

// 定义合约abi
var abi = [{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}];

// 定义合约地址（在部署时可以看到, truffle migrate --reset)
var address = "0x781DaC401c06655Df8F0a0C763467f328083ed53"

// 得到合约实例
var Instance = new web3.eth.Contract(abi,address)

// get 方法调用
Instance.methods.get().call().then((value)=>{console.log(value)})

// set 方法调用 （在终端中不能选钱包地址，不可见，可以选account[0]）
Instance.methods.set(323).send({ from: "0xde560d0fac79e7d35e58bbf3bb2f138586975ecc" }).then(()=>{console.log("set")})

