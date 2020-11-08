const fs = require('fs')
const lib = require('./lib')(require('./config'))

async function main() {
  let factory = lib.contract('0x16cf9e5a5848E40E27751f1c9277291993fE6C4E', JSON.parse(fs.readFileSync('GetStartedFactory.abi')))
  let instance_address = await factory.view('instances', lib.account.address)

  if(instance_address === '0x0000000000000000000000000000000000000000') {
    await factory.call('create')
    instance_address = await factory.view('instances', lib.account.address)
  }

 //factory.call('create')
 console.log(`instance = ${instance_address}`)
 let instance = lib.contract(instance_address, JSON.parse(fs.readFileSync('GetStarted.abi')))
 await instance.call('callme')
}

main()
