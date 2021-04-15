import requests
from pprint import pprint 
API_HOST = 'https://api.bitkub.com'
res_ticket = requests.get(API_HOST + '/api/market/ticker').json()
res_symbols = requests.get(API_HOST + '/api/market/symbols').json()['result']

class Bitkub:
    def getCoin():
        return  ''

    def getSymbols():
        symbols=[]
        for i in res_symbols:
            symbols.append(i['symbol'])
        return symbols
    
    def coins():
        coins=[]
        for i in res_symbols:
            if i['symbol'] != 'THB_CTXC' and i['symbol'] != 'THB_DON' :
                coins.append({"symbols":i['symbol'],"price":res_ticket[i['symbol']]['last']})
        return coins
