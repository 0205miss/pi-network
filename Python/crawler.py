from stellar_sdk import Server
server = Server(horizon_url="https://api.mainnet.minepi.com/")
"""
You can set to 
last_cursor = "15889776972406785"
account = 843810
lock = 685523443.91551
circulate = 31376828.3255129
pending_failed = 1279
tx_pioneer = 302291.9877727
"""
last_cursor = "14442085230841856"
account = 0
lock = 0
circulate = 0
pending_failed = 0
tx_pioneer = 0
ct_account = ['GBQQRIQKS7XLMWTTRM2EPMTRLPUGQJDLEKCGNDIFGTBZG4GL5CHHJI25',
              'GDPDSLFVGEPX6FJKGZXSTJCPTSKKAI4KBHBAQCCKQDXISW3S5SJ6MGMS',
              'GABT7EMPGNCQSZM22DIYC4FNKHUVJTXITUF6Y5HNIWPU4GA7BHT4GC5G',
              'GC5RNDCRO6DDM7NZDEMW3RIN5K6AHN6GMWSZ5SAH2TRJLVGQMB2I3BNJ',
              'GDPDSLFVGEPX6FJKGZXSTJCPTSKKAI4KBHBAQCCKQDXISW3S5SJ6MGMS',
              'GB7HLN74IIY6PENSHHBBJJXWV6IZQDELTBZNXXORDGTL75O4KC5CUXEV']
def tx_handler(tx_response):
    global account,lock,circulate,pending_failed,tx_pioneer,ct_account
    if(tx_response['type']=='payment'):
        if(tx_response['from'] in ct_account):
            pass
        else:
            tx_pioneer = round(float(tx_pioneer) + float(tx_response['amount']),7)
    else:
        if(tx_response['type']=='create_account' and tx_response['starting_balance']=="1.0000000"):
            account +=1
        if(tx_response['type']=='create_claimable_balance'):
            lock = round(float(lock) + float(tx_response['amount']),7)
        if(tx_response['type']=='claim_claimable_balance' and tx_response['source_account']!='GC5RNDCRO6DDM7NZDEMW3RIN5K6AHN6GMWSZ5SAH2TRJLVGQMB2I3BNJ'):
            a = server.effects().for_operation(tx_response['id']).call()["_embedded"]["records"][0]["amount"]
            lock = round(float(lock) - float(a),7)
            circulate = round(float(circulate) + float(a),7)
        if(tx_response['type']=='claim_claimable_balance' and tx_response['source_account']=='GC5RNDCRO6DDM7NZDEMW3RIN5K6AHN6GMWSZ5SAH2TRJLVGQMB2I3BNJ'):
            a = server.effects().for_operation(tx_response['id']).call()["_embedded"]["records"][0]["amount"]
            lock = round(float(lock) - float(a),7)
            pending_failed += 1        
        print(f"op_id:{tx_response['id']}\n create account:{account}\n lock:{lock}\n circulate:{circulate}\n CT_claimback:{pending_failed}\n Pioneer Total Transfer:{tx_pioneer}")

if __name__ == '__main__':
    for tx in server.operations().cursor(last_cursor).stream():
        tx_handler(tx)
