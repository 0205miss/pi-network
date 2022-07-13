from stellar_sdk import Server
import json
server = Server(horizon_url="https://api.mainnet.minepi.com/")
"""
You can set to 
last_cursor = "15748631462158337"
account = 813282
lock = 689048965.7415967
circulate = 7381148.4734841
"""
last_cursor = "14442085230841856"
account = 0
lock = 0
circulate = 0
def tx_handler(tx_response):
    global account,lock,circulate
    if(tx_response['type']=='create_account' and tx_response['starting_balance']=="1.0000000"):
        account +=1
    if(tx_response['type']=='create_claimable_balance'):
        lock = round(float(lock) + float(tx_response['amount']),7)
    if(tx_response['type']=='claim_claimable_balance' and tx_response['source_account']!='GABT7EMPGNCQSZM22DIYC4FNKHUVJTXITUF6Y5HNIWPU4GA7BHT4GC5G'):
        a = server.effects().for_operation(tx_response['id']).call()["_embedded"]["records"][0]["amount"]
        lock = round(float(lock) - float(a),7)
        circulate = round(float(circulate) + float(a),7)
    if(tx_response['type']=='claim_claimable_balance' and tx_response['source_account']=='GABT7EMPGNCQSZM22DIYC4FNKHUVJTXITUF6Y5HNIWPU4GA7BHT4GC5G'):
        a = server.effects().for_operation(tx_response['id']).call()["_embedded"]["records"][0]["amount"]
        lock = round(float(lock) - float(a),7)
    print(f"op_id:{tx_response['id']}\n create account:{account}\n lock:{lock}\n circulate:{circulate}")

if __name__ == '__main__':
    for tx in server.operations().cursor(last_cursor).stream():
        tx_handler(tx)
