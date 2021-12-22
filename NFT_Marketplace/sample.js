async function nft(){
  const sourceSecretKey = 'secret key';
  const sourceKeypair = StellarSdk.Keypair.fromSecret(sourceSecretKey);
  const sourcePublicKey = sourceKeypair.publicKey();
  const issuer = StellarSdk.Keypair.random();
  const server = new StellarSdk.Server('https://api.testnet.minepi.com/');
  const account = await server.loadAccount(sourcePublicKey);
  const fee = await server.fetchBaseFee();
  const asset = new StellarSdk.Asset("nft",issuer.publicKey()) //asset type code
  const transaction = new StellarSdk.TransactionBuilder(account,{fee,networkPassphrase:"Pi Testnet"})
  .addOperation(StellarSdk.Operation.createAccount({
  destination:issuer.publicKey(),
  startingBalance: ""  //need base serve * 3
  }))
  .addOperation(StellarSdk.Operation.changeTrust({
  asset:asset
  }))
  .addOperation(StellarSdk.Operation.payment({
  destination:sourceKeypair.publicKey(),
    asset:asset,
    amount:"",//nft amount
    source:issuer.publicKey()
  }))
  .addOperation(StellarSdk.Operation.manageData({
    name:"ipfs",
    value:"",//ipfs_hash
    source:issuer.publicKey()
  }))
  .addOperation(StellarSdk.Operation.setOptions({
    masterWeight:"0",
    homeDomain:"",//stellar.toml host domain
    source:issuer.publicKey()
  }))
  .setTimeout(30)
  .build();
  transaction.sign(sourceKeypair);
  transaction.sign(issuer);
const transactionResult = await server.submitTransaction(transaction);
console.log(transactionResult);
console.log(issuer.publicKey());
}
