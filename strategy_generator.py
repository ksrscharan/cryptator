# strategy_generator.py
import ccxt

class GeneticAlgorithmStrateyGenerator:

    def __init__(self, exchange_name):
        if exchange_name.lower() == 'binance':
            self.exchange = ccxt.binance()
        elif exchange_name.lower() == 'bybit':
            self.exchange = ccxt.bybit()
        elif exchange_name.lower() == 'bitget':
            self.exchange = ccxt.bitget()
        self.exchange.load_markets()

    def generate_strategy(self, symbol, timeframe, limit):
        ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, limit)
            
        if not ohlcv:
            print(f"No OHLCV data fetched for {symbol} on {timeframe}.")
            return None
        return ohlcv

    def arrange_data(self, ohlcv):
        arranged_data = []
        for candle in ohlcv:
            timestamp, open_price, high, low, close, volume = candle
            arranged_data.append({
                'timestamp': timestamp,
                'open': open_price,
                'high': high,
                'low': low,
                'close': close,
                'volume': volume
            })

        return arranged_data