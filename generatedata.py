import pandas as pd
import numpy as np 
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import timedelta, date

def getData():

    # Fetch historical data 
    symbols = {"VHT" : "Financial",
                "VNQ" : "Real Estate",
                "VDC" : "Consumer Staples", 
                "VCR" : "Consumer Discretionary",
                "VGT" : "Information Technology"}

    start_date = '2015-01-01'
    end_date = date.today()
    rdata = yf.download(list(symbols.keys()), start=start_date, end=end_date)
    data = pd.DataFrame()

    print("Generating data table...")
    for key in symbols.keys():
        data['Weekly Change - ' + symbols.get(key)] = (rdata['Close'][key].pct_change(7) * 100).round(2)
        data['Monthly Change - ' + symbols.get(key)] = (rdata['Close'][key].pct_change(30) * 100).round(2)
        data['SMA 50 - '+symbols.get(key)] = (rdata['Close'][key].rolling(window=50).mean()).round(2)
        data['SMA 200 - '+symbols.get(key)] = (rdata['Close'][key].rolling(window=200).mean()).round(2)
        data['SMA Deviation - '+symbols.get(key)] = (data['SMA 50 - '+symbols.get(key)] / data['SMA 200 - '+symbols.get(key)]).round(2)

    lastRow = pd.DataFrame(data.iloc[-1])
    # data.iloc[-1].to_markdown('data.md')
    lastRow.to_html('data.html')

    # Plot both cumulative returns on the same chart 
    plt.figure(figsize=(12, 6)) 
    plt.title('Industry Sector Performance (Simple Mean Average - 50 days)')
    plt.xlabel('Date') 
    plt.ylabel('Price') 
    for key in symbols.keys():
        plt.plot(data.index, data['SMA 50 - '+symbols.get(key)], label=symbols[key])
    plt.legend()
    plt.savefig('graph.png')
