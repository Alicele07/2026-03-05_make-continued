import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/data.csv')
plt.plot(df['x'], df['y'])
plt.savefig('results/plot.png')
print("Plot saved!")