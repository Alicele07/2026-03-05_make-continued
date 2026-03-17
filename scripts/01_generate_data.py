import pandas as pd
import numpy as np

# Generate random walk data
df = pd.DataFrame({'x': range(100), 'y': np.random.randn(100).cumsum()})
df.to_csv('data/data.csv', index=False)
print("Data generated!")