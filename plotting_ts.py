import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

for file in glob('../data/binance/*'):
    df = pd.read_parquet(file)
    exchange = file[16:-8]
    plt.figure(figsize=[16,8])
    plt.title(exchange)
    plt.plot(df['close'], lw=2)
    plt.savefig(f'time_series/{exchange}')
    plt.close()
