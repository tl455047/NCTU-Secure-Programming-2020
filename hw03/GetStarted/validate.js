const fs = require('fs')
const lib = require('./lib')(require('./config'))

async function main() {
  let factory = lib.contract('0x16cf9e5a5848E40E27751f1c9277291993fE6C4E', JSON.parse(fs.readFileSync('GetStartedFactory.abi')))
  await factory.call('validate', '0x84f044be2b6c6a64e6062e968aa0c2847d0aedf79d5d158d223fa6d94d0c25b3')
}

main()
