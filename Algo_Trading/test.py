import oandapy as opy
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()

oanda = opy.API(environment='practice',
                access_token= "2d45e798880ca7ea9d44cb3fa9d03b72-a755329fa17704aa4328136b1366b166")

class MyStreamer(opy.Streamer):
    def __init__(self, count=10, *args, **kwargs):
        super(MyStreamer, self).__init__(*args, **kwargs)
        self.count = count
        self.reccnt = 0

    def on_success(self, data):
        print (data, "\n")
        self.reccnt += 1
        if self.reccnt == self.count:
            self.disconnect()

    def on_error(self, data):
        self.disconnect()


account = "ianx0114"
stream = MyStreamer(environment="practice", 
                    access_token="2d45e798880ca7ea9d44cb3fa9d03b72-a755329fa17704aa4328136b1366b166")
stream.rates(account, instruments="EUR_USD,EUR_JPY,US30_USD,DE30_EUR")

response = oanda.get_prices(instruments="EUR_USD")
prices = response.get("prices")
asking_price = prices[0].get("ask")

print(asking_price)