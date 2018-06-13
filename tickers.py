import os

class Tickers():
    def __init__(self):
        self.ticker_dict = {}

    def update_tick(self,sym,price):
        self.ticker_dict[sym] = price

    def top_ticks(self,num_top):
        top_price = 0
        top_sym = None
        top_ticks = []
        temp_ticker = self.ticker_dict
        print (temp_ticker)
        for x in range(0,num_top):
            for sym,price in temp_ticker.items():
                if price > top_price:
                    top_price = price 
                    top_sym = sym
            top_ticks.append((top_sym, top_price))
            temp_ticker.pop(top_sym)
            top_price = 0
            top_sym = None
        return top_ticks

if __name__=='__main__':
    new_tickers = Tickers()
    new_tickers.update_tick('aapl',100)
    new_tickers.update_tick('msft',105)
    new_tickers.update_tick('goog',200)
    new_tickers.update_tick('ttwo',20)
    new_tickers.update_tick('cake',10)
    new_tickers.update_tick('ibm',50)
    new_tickers.update_tick('face',150)
    new_tickers.update_tick('amzn',300)
    new_tickers.update_tick('att',75)
    new_tickers.update_tick('vzw',70)

    print (new_tickers.top_ticks(5))


