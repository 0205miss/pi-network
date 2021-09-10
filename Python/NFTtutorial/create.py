from stellar_sdk import Server, Keypair, TransactionBuilder, Network, ManageSellOffer, Asset
from mnemonic import Mnemonic
import requests
server = Server("http://127.0.0.1:31401/")
base_fee = server.fetch_base_fee()
passphrase = '私鑰(註記詞)'
my_passphrase = '' 
my_language = 'english'
mnemo = Mnemonic(my_language)
if mnemo.check(friend):
    friend_seed = Mnemonic.to_seed(passphrase, my_passphrase)
from keyfunc import account_keypair
account_number = 0
ff = account_keypair(friend_seed, account_number)
friendt_key = Keypair.from_secret(ff.seed().decode())
print(ff.seed().decode())
issuer_public_key = friendt_key.public_key
destination = Keypair.random()
source_account = server.load_account(account_id=friendt_key.public_key)
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase="Pi Testnet",
        base_fee=base_fee,
    )
    .append_create_account_op(
        destination=destination.public_key,
        starting_balance="31"
    )
    .build()
)
transaction.sign(friendt_key)
response = server.submit_transaction(transaction)
print(
    f"New Keypair: \n\t public: {destination.public_key}\n\t  secret: {destination.secret}"
)
