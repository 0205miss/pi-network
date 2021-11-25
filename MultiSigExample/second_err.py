from stellar_sdk import Server, Keypair, TransactionBuilder, Network,Signer
source_keypair = Keypair.from_secret("SBS3XF56PTYY65BXBY4GZGPQHODXTSRU6D75MD3GK6D64BEU3IGRVPSA")
server = Server("https://api.testnet.minepi.com/")
source_account = server.load_account("GCQYJHOTTFGSHIUYULUGNELRZMC3UFRC4EVHWNT7GBXOXUTBESBE24AG")
base_fee = server.fetch_base_fee()
transaction = (
        TransactionBuilder(
            source_account=source_account,
            network_passphrase="Pi Testnet",
            base_fee=base_fee,
        )
        .append_payment_op("GCSXRBF3YP4NVB7XP2C35O6TWYUQTARNVYR5U6S2JI7RJFWP5JXC5XTY", "0.00001", "XLM")
        .build()
    )
transaction.sign(source_keypair)
response = server.submit_transaction(transaction)
print(response)