import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

apple = yf.download('AAPL')
nvidia = yf.download('NVDA')
amd = yf.download('AMD')
microsoft = yf.download('MSFT')
intel = yf.download('INTC')

data = pd.concat([apple, nvidia, amd, microsoft, intel], axis = 1, join = 'inner')

data_adj = data['Adj Close']
data_adj.columns = ['APPLE', 'NVIDIA', 'AMD', 'MICROSOFT', 'INTEL']
data_adj.plot()
plt.title("Adj Close")

reward_daily = data_adj / data_adj.shift(1)
reward_daily.plot()
plt.title("Daily Reward")

reward_total = (data_adj / data_adj.shift(1)).cumprod()
reward_total.plot()
plt.title("Total Reward")