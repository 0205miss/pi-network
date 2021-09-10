from stellar_sdk import Server,Keypair,TransactionBuilder, Network ,Asset
import requests
server = Server("http://127.0.0.1:31401/")#https://api.testnet.minepi.com/
fee = server.fetch_base_fee()
network = "Pi Testnet"
account = server.load_account("GCUQCXPUX5WT3NOA5VJTLM35OCG4KVXCF3K7TYEEX377J2OD6O36OP5C")
secret = Keypair.from_secret("SBZ33W7TBKT3LILEF44JZ6J3PJM5P2N63I423WB72PTF5TALWSYSGXZP")
transaction=(
    TransactionBuilder(
        source_account = account,
        network_passphrase = network,
        base_fee = fee
    )
    .append_set_options_op(
        inflation_dest="GCUQCXPUX5WT3NOA5VJTLM35OCG4KVXCF3K7TYEEX377J2OD6O36OP5C",
        master_weight = 0        
        )
    .build()
)
transaction.sign(secret)
res = server.submit_transaction(transaction)
