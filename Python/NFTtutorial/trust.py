from stellar_sdk import Server,Keypair,TransactionBuilder, Network ,Asset
import requests
server = Server("http://127.0.0.1:31401/")#https://api.testnet.minepi.com/
fee = server.fetch_base_fee()
network = "Pi Testnet"
user_public_key = "GAT55X4HMQ5W4OXH77P6GAXMJJI5TW3KBZEK45WUDKCB4CYFBJGJBO5H"
user_account = server.load_account(account_id=user_public_key)
user_secret = Keypair.from_secret("SCW66AECE7J7NQI6QLP2R3BBHVT6WJ5DW7JXGFADVHPIBF35OTB32LBO")
asset_coin = Asset("TutorialNFT","GCUQCXPUX5WT3NOA5VJTLM35OCG4KVXCF3K7TYEEX377J2OD6O36OP5C")
transaction=(
    TransactionBuilder(
        source_account = user_account,
        network_passphrase = network,
        base_fee = fee
    )
    .append_change_trust_op(
        asset_code = asset_coin.code,
        asset_issuer = asset_coin.issuer,
        limit="0.0000001"
        )
    .build()
    )
transaction.sign(user_secret)
response = server.submit_transaction(transaction)
