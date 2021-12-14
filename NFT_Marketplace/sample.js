async function nft(){
  const StellarSdk = require('stellar-sdk');
  const sourceSecretKey = '';
  const sourceKeypair = StellarSdk.Keypair.fromSecret(sourceSecretKey);
  const sourcePublicKey = sourceKeypair.publicKey();
  const issuer = StellarSdk.Keypair.random();
  const server = new StellarSdk.Server('127.0.0.1');
  const account = await server.loadAccount(sourcePublicKey);
  const fee = await server.fetchBaseFee();
  const asset = new StellarSdk.Asset(code,issuer.publicKey())
  const transaction = new StellarSdk.TransactionBuilder(account,{fee,networkPassphrase:"Pi Testnet"})
  .addOperation(StellarSdk.Operation.createAccount(
  destination:issuer.publicKey(),
  startingBalance: {base reverse*3}
  ))
  .addOperation(StellarSdk.Operation.changeTrust(
  asset:asset
  ))
  .addOperation(StellarSdk.Operation.payment(
  destination:sourcePublicKey,
    asset:asset,
    amount:?,
    source:issuer.publicKey()
  ))
  .addOperation(StellarSdk.Operation.manageData(
    name:"ipfs",
    value:ipfs_hash,
    source:issuer.publicKey()
  ))
  .addOperation(StellarSdk.Operation.setOptions(
    masterWeight:0,
    homeDomain:?
  ))
}
