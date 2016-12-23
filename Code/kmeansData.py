import pandas as pd
from numpy import *
import numpy as np



stock_data = pd.read_csv('/Users/Pattorio/Documents/BigData_dataset/FinalProject/WIKI_PRICES.csv', parse_dates=[1])


#volumn
volume = stock_data.groupby(stock_data['ticker']).mean()
volume_vol = volume['volume']
print(volume_vol.size)

#pct_Change
pctChange = stock_data.groupby(stock_data['ticker']).pct_change()
pctChange['ticker'] = stock_data['ticker']
pctChange = pctChange.groupby(pctChange['ticker']).mean()
pctChange_close = pctChange['adj_close']
print(pctChange_close.size)

#amplitude
temp = (stock_data['adj_high'] - stock_data['adj_low'])/stock_data['adj_close']
amplitude = pd.DataFrame(columns=['ticker', 'amplitude'])
amplitude['ticker'] = stock_data['ticker']
amplitude['amplitude'] = temp

dayAmp = amplitude.groupby(amplitude['ticker']).mean()
amp = dayAmp['amplitude']
print(amp.size)

vector = vstack((volume_vol, pctChange_close, amp))
print(vector.size)


np.savetxt('/Users/Pattorio/Documents/BigData_dataset/FinalProject/vector.txt', vector)




#pctChange.to_csv('/Users/Pattorio/Documents/BigData_dataset/FinalProject/pctChange.csv', index=False)
#amp.to_csv('/Users/Pattorio/Documents/BigData_dataset/FinalProject/amp.csv', index=False)