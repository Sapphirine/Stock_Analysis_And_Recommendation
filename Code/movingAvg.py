import pandas as pd

stock_data = pd.read_csv('/Users/Pattorio/Documents/BigData_dataset/FinalProject/ADES.csv', parse_dates=[1])
stock_data.sort_values(['date'], inplace=1)
ma_list = [5, 20, 60]
for ma in ma_list:
    stock_data['MA_' + str(ma)] = stock_data['close'].rolling(window=ma).mean()

stock_data.sort_values(['date'], ascending=0, inplace=1)
stock_data.to_csv('/Users/Pattorio/Documents/BigData_dataset/FinalProject/ADES_movingAge.csv', index=False)
