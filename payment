#  pay 10.25 Pi
from stellar_sdk import Server, Keypair, TransactionBuilder, Network
from mnemonic import Mnemonic
my_seed_phrase = 'passphrase'
my_passphrase = '' 
my_language = 'english' # or other language listed in
                            # https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md
mnemo = Mnemonic(my_language)
if mnemo.check(my_seed_phrase):
# my_seed_phrase is a valid BIP39 phrase for my_language   
    binary_seed = Mnemonic.to_seed(my_seed_phrase, my_passphrase)
from keyfunc import account_keypair
account_number = 0 # an small unsigned integer (0 for the primary account)
kp = account_keypair(binary_seed, account_number)
source_keypair = Keypair.from_secret(kp.seed().decode())
des_address = "GBFA4NMHFUGHUV2QNGKNEFDS5IC64BWU5HDSWTDFI3EWRUPRXRRRFMPY" #destination address
server = Server("https://api.testnet.minepi.com/")
source_account = server.load_account(source_keypair.public_key)
base_fee = server.fetch_base_fee()
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase="Pi Testnet",
        base_fee=base_fee,
    )
    .add_text_memo("Hello, PiNetwork!")
    .append_payment_op(des_address, "10.25", "XLM") # xlm = native base on stellar sdk setting and will be pi in pi blockchain
    .build()
)
transaction.sign(source_keypair)
response = server.submit_transaction(transaction)
