var pubkey
var privkey 
    async function key(){
      var mnemonics = { "english": new Mnemonic("english") };
        var mnemonic = mnemonics["english"];
        var phrase = document.getElementById('key').value;
        seed = mnemonic.toSeed(phrase, "");
        var path = "m/44'/314159'/0'";
        var keypair = libs.stellarUtil.getKeypair(path, seed);
        indexText = path;
        privkey = StellarSdk.Keypair.fromSecret(keypair.secret());
        pubkey  = keypair.publicKey();
        document.getElementById("s0").innerHTML='解鎖';
    };
    async function trust() {
        const server = new StellarSdk.Server('https://api.testnet.minepi.com/');
        const fee = 100000;
        const account = await server.loadAccount(pubkey);
        console.log(fee);
        const trustchange = new StellarSdk.TransactionBuilder(account, {
            fee,
            networkPassphrase: 'Pi Testnet'
          })
          .addOperation(StellarSdk.Operation.changeTrust({
            asset: new StellarSdk.Asset('PAPC','GBFA4NMHFUGHUV2QNGKNEFDS5IC64BWU5HDSWTDFI3EWRUPRXRRRFMPY'),
            limit: '1',
          }))
          .setTimeout(100)
          .build();
          trustchange.sign(privkey);
          server.submitTransaction(trustchange);
          cooldown();
          document.getElementById("s1").innerHTML='已執行';
        }
      async function buy(){
		const server = new StellarSdk.Server('https://api.testnet.minepi.com/');
        const fee = 100000;
        account = await server.loadAccount(pubkey);
        const buyoffer = new StellarSdk.TransactionBuilder(account, {
            fee,
            // Uncomment the following line to build transactions for the live network. Be
            // sure to also change the horizon hostname.
            // networkPassphrase: StellarSdk.Networks.PUBLIC,
            networkPassphrase: 'Pi Testnet'
          })
          // Add a payment operation to the transaction
          .addOperation(StellarSdk.Operation.manageBuyOffer({
            selling:StellarSdk.Asset.native(),
            buying:new StellarSdk.Asset('PAPC','GBFA4NMHFUGHUV2QNGKNEFDS5IC64BWU5HDSWTDFI3EWRUPRXRRRFMPY'),
            buyAmount:'1',
            price:'1',
          }))
          // Make this transaction valid for the next 30 seconds only
          .setTimeout(100)
          // Uncomment to add a memo (https://www.stellar.org/developers/guides/concepts/transactions.html)
          // .addMemo(StellarSdk.Memo.text('Hello world!'))
          .build();
          buyoffer.sign(privkey);
          server.submitTransaction(buyoffer);
          cooldown();
          document.getElementById("s2").innerHTML='已執行';
    };
    async function sell(){
		const server = new StellarSdk.Server('https://api.testnet.minepi.com/');
        const fee = 100000;
      account = await server.loadAccount(pubkey);
      const buyoffer = new StellarSdk.TransactionBuilder(account, {
        fee,
        networkPassphrase: 'Pi Testnet'
      })
      .addOperation(StellarSdk.Operation.payment({
        destination:'GAHVUXJEP2BENC5AFGJI4XKTLPYO3TICGODOF5KTQV5BHWS3BBDLCC6O',
        asset: new StellarSdk.Asset('PAPC','GBFA4NMHFUGHUV2QNGKNEFDS5IC64BWU5HDSWTDFI3EWRUPRXRRRFMPY'),
        amount:'1',
      }))
      .setTimeout(100)
      .build();
      buyoffer.sign(privkey);
      server.submitTransaction(buyoffer);
      cooldown();
      document.getElementById("s3").innerHTML='已執行';
};
    async function del_trust(){
		const server = new StellarSdk.Server('https://api.testnet.minepi.com/');
        const fee = 100000;
      account = await server.loadAccount(pubkey);
      const del_trust = new StellarSdk.TransactionBuilder(account, {
        fee,
        networkPassphrase: 'Pi Testnet'
      })
      .addOperation(StellarSdk.Operation.changeTrust({
        asset: new StellarSdk.Asset('PAPC','GBFA4NMHFUGHUV2QNGKNEFDS5IC64BWU5HDSWTDFI3EWRUPRXRRRFMPY'),
        limit: '0',
      }))
      .setTimeout(100)
      .build();
      del_trust.sign(privkey);
      server.submitTransaction(del_trust);
      cooldown();
      document.getElementById("s4").innerHTML='已執行';
    };
    function browse(){
        var link = 'https://pi-blockchain.net/account/'+pubkey;
        window.location.href=link;
    }
    function cooldown(){
      const b1 = document.getElementById('b1');
      const b2 = document.getElementById('b2');
      const b3 = document.getElementById('b3');
      const b4 = document.getElementById('b4');
      b1.disabled = true;
      b2.disabled = true;
      b3.disabled = true;
      b4.disabled = true;
      setTimeout(function(){
      b1.disabled = false;
      b2.disabled = false;
      b3.disabled = false;
      b4.disabled = false;
      },5000);
    }
