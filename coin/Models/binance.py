from binance.client import Client
import time
from binance.websockets import BinanceSocketManager

api_key = "GjC5Rqmf0WqWBcpVznUiEYvrLLZfhaQ6SlvhFKds8AxEanUBHRMQtpZja2RRJciz"
api_secret = "MJjXkyPNrtmmNLB2ucZy80Y3cExL2GCp3S8zfoAWCDg570QMcxLOHPVBi3F4foMp"
client = Client(api_key, api_secret)

class data:
    x=10
    
    def trade():
        price = client.get_all_tickers()
        allprice = []
        for p in price:
            if p['symbol'] == 'WANUSDT':
                allprice.push(p)
            if p['symbol'] == 'IOSTUSDT':
                allprice.push(p)
            if p['symbol'] == 'NEARUSDT':
                allprice.push(p)
                return p
    
    def dept():
        klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
        dept = client.get_order_book(symbol='BNBUSDT')
        return klines
    