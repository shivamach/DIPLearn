import pandas as pd

# imports done
# import quandl, used quandl to get the dataset and already stored it so dont have to worry bout
# it

df = pd.read_csv("google_wiki.csv")
# only taking the adjusted prices that adjust for splits and merge of stock
# we want to feed features meaningful into regression
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = ((df['Adj. High'] - df['Adj. Close']) / df['Adj. Close']) * 100.0
# this gives an idea about how volatile the stock prices have been
df['PCT_change'] = ((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']) * 100.0
# daily change between/ variation of opening and closing prices of these stocks
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head())
