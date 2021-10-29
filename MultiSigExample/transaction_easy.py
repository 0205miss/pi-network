from stellar_sdk import Server, Keypair, TransactionBuilder, Network
source_keypair = Keypair.from_secret("SCSBOMWKMC4D73BYO6SRLYH6W5HZWLCTJYRGXHYMUSIJ424I3B3SPCZI") #員工2
des_address = "GAPHBNK4YXFXCTVKFRX3T6NK5UFXL3QZ4TTTZFNBKJYVJX7TUWX5E5TC" #員工1
two_key = Keypair.from_secret("SBYERBXPHFDSILTGXHSGRH6QN64G3EZEUQF5I3YXHKRNEC363UFKBHRC") #員工3
server = Server("http://127.0.0.1:31401")
source_account = server.load_account(source_keypair.public_key)
base_fee = server.fetch_base_fee()
transaction = (
        TransactionBuilder(
            source_account=source_account,
            network_passphrase="Pi Testnet",
            base_fee=base_fee,
        )
        .add_text_memo("Play By Pionner:0205miss")
        .append_payment_op(des_address, "0.0000001", "XLM")
        .append_set_options_op(source="GD2UYRQCNMF6AFMAWZSE6HNNRUPKSUCJJ3V7YYZRM76WV77F3XF5P6FN")
        .build()
    )
transaction.sign(source_keypair)
transaction.sign(two_key)
response = server.submit_transaction(transaction)
print(response)
