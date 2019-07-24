#!/bin/sh
geth --datadir /workspace/data88/ --networkid 88 --rpc --rpcaddr "0.0.0.0" --rpcport 8989 -port 28000 --rpcapi admin,eth,miner,web3,personal,net,txpool --allow-insecure-unlock --rpccorsdomain '*' --nodiscover 
sleep 3888888
