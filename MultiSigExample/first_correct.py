from stellar_sdk import Server, Keypair, TransactionBuilder, Network,Signer
source_keypair = Keypair.from_secret("SAG4GAUTCJMWHTD5J2EKV26W5YSCGPV3VEGFY4I4VDZMO67L3VKSRQKH")
server = Server("https://api.testnet.minepi.com/")
source_account = server.load_account("GAKEGUBP6CIPIUFJ46ZXDAJTZOEE3PMVYOD4VSN32DFFNMX427V73DMJ")
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
