import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

mediatek = yf.download('2454.TW')
tsmc = yf.download('2330.TW')
umc = yf.download('2303.TW')
foxconn = yf.download('2317.TW')
quanta = yf.download('2382.TW')
wistron = yf.download('3231.TW')

data = pd.concat([mediatek, tsmc, umc, foxconn, quanta, wistron], axis = 1, join = 'inner')

data_adj = data['Adj Close']
data_adj.columns = ['MediaTek', 'TSMC', 'UMC', 'Foxconn', 'Quanta', 'Wistron']
data_adj.plot()
plt.title("Adj Close")

reward_daily = data_adj / data_adj.shift(1)
reward_daily.plot()
plt.title("Daily Reward")

reward_total = (data_adj / data_adj.shift(1)).cumprod()
reward_total.plot()
plt.title("Total Reward")