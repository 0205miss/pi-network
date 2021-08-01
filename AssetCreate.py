from stellar_sdk import Server, Keypair, TransactionBuilder, Network, ManageSellOffer, Asset
from mnemonic import Mnemonic
import requests
server = Server("https://api.testnet.minepi.com/")
base_fee = server.fetch_base_fee()
issuer_phrase = 'issuer passphrase' #need to change
seller_phrase = 'seller passphrase' #need to change
my_passphrase = '' 
my_language = 'english'
mnemo = Mnemonic(my_language)
if mnemo.check(issuer_phrase):
    issuer_seed = Mnemonic.to_seed(issuer_phrase, my_passphrase)
if mnemo.check(seller_phrase):
    seller_seed = Mnemonic.to_seed(seller_phrase,my_passphrase)
from keyfunc import account_keypair
account_number = 0 # an small unsigned integer (0 for the primary account)
issuer = account_keypair(issuer_seed, account_number)
seller = account_keypair(seller_seed, account_number)
seller_secret_key = Keypair.from_secret(seller.seed().decode())
issuer_secret_key = Keypair.from_secret(issuer.seed().decode())
issuer_public_key = issuer_secret_key.public_key
seller_public_key = seller_secret_key.public_key
issuer_account = server.load_account(account_id=issuer_public_key)
seller_account = server.load_account(account_id=seller_public_key)
#manage offer
network_passphrase = "Pi Testnet"
## get fee from Pi Testnet
fee = base_fee
print("\nCreate new Asset\n")
# create asset

## Create an object to represent the new asset
asset_coin = Asset("PAPC", issuer_public_key) #You can change PAPC to what you want. Mention that the letters must<=12 

## The Seller Account (the account that the custom asset receivs) must trust the asset.
print(
    "The Seller Account must trust the new asset. \
      \nCreate Trust."
)
trust_transaction = (
    TransactionBuilder(
        source_account=seller_account,
        network_passphrase=network_passphrase,
        base_fee=fee,
    )
    #  The `changeTrust` operation creates (or alters) a trustline
    #  The `limit` parameter below is optional
    .append_change_trust_op(
        asset_code=asset_coin.code,
        asset_issuer=asset_coin.issuer,
        limit="5000", #this is the limit for your token, you can create more in future if your issuer account is not in lock status
    )
    .set_timeout(100)
    .build()
)

trust_transaction.sign(seller_secret_key)
trust_transaction_resp = server.submit_transaction(trust_transaction)
print("Trust created\n")
## Send 5000 PAPC asset to the seller account.
print("Send PAPC to seller account")
aac_payment_transaction = (
    TransactionBuilder(
        source_account=issuer_account,
        network_passphrase=network_passphrase,
        base_fee=fee,
    )
    .append_payment_op(
        destination=seller_public_key,
        amount="5000",
        asset_code=asset_coin.code,
        asset_issuer=asset_coin.issuer,
    )
    .build()
)
aac_payment_transaction.sign(issuer_secret_key)
aac_payment_transaction_resp = server.submit_transaction(aac_payment_transaction)
print(f"Sended 5000 PAPC to {seller_public_key}")
print("#" * 30)
