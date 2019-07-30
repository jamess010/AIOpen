1) mkdir -p 'dir', and cd to 'dir', and run "truffle unbox react"
2) copy ./source/App.js to "./client/src/App.js" , and copy ./source/truffle-config.js to ./
3) copy ./source/Migration.sol ./source/SimpleStorage.sol to "contracts"
4) copy ./source/1_initial_migration.js	./source/2_deploy_contracts.js to "migrations"
5) truffle develop (port: 8545)
6) compile
7) migrate (--reset)
8) cd client, npm start
9) config metamask wallet , and connect to private chain on http://localhost:8545, if wallet is no ETH, send some ETH from coinbase account to wallet account
10) visit http://localhost:3000
11) input nuber in input box, then click "Update" button
12) in wallet , click comfirm button
13) in mainpage ,the The stored value is: xxx(you enter number above) 
