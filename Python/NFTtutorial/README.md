# pi-network
Create NFT BY Python

You should install some library
keyfunc.py should put in the same folder

``pip install mnemonic``

``pip install stellar-sdk==4.1.0``

Need to prepare

  two account(issuer and seller)
  
  the base test pi in issuer >30.0x (that base on how much operation you need)
  
# Flow

create.py --> 

trust.py(change trust) --> 

send.py(payment) --> 

manage.py(data operation) --> 

lock.py(not necessary step, only for stopping issuing)

# Mention
Server should change to ``https://api.testnet.minepi.com/`` if you don't have a node api service.

It is possible to bind the operation together by using multiple `.append_operation(operation)`
