const fs = require('fs')
const lib = require('./lib')(require('./config'))

async function main() {
  let instance = lib.contract('0x21546f53ac81ddfc2b618d5617d173e43661366c', JSON.parse(fs.readFileSync('Private.abi')))
  console.log(await instance.storage(0));
}

main()
