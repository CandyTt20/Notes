import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataf = pd.read_csv(r'F:\dataexample\alipay.csv')

# print(dataf.loc[:, 'y'])
y = list(dataf.loc[:, 'y'])
x = [i for i in range(len(y))]
# print(dataf)
plt.plot(x, y)
plt.show()
