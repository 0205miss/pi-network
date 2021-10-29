from stellar_sdk import Server, Keypair, TransactionBuilder, Network,Signer
source_keypair = Keypair.from_secret("SBS3XF56PTYY65BXBY4GZGPQHODXTSRU6D75MD3GK6D64BEU3IGRVPSA")
server = Server("https://api.testnet.minepi.com/")
source_account = server.load_account("GD5NOLDZ6FVB762P5IORKUWFHATH4A53CMOX5HJD47UI74Q7ZQWH6NFP")
base_fee = server.fetch_base_fee()
signer = Signer.ed25519_public_key(account_id="GAPHBNK4YXFXCTVKFRX3T6NK5UFXL3QZ4TTTZFNBKJYVJX7TUWX5E5TC",weight=1)
transaction = (
        TransactionBuilder(
            source_account=source_account,
            network_passphrase="Pi Testnet",
            base_fee=base_fee,
        )
        .append_set_options_op(
            
            signer=signer
            )
        .build()
    )
transaction.sign(source_keypair)
response = server.submit_transaction(transaction)
print(response)
