import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#! Mathematica: Export["out01.csv", Table[{theta, 5 Sin[theta]}, {theta, 0, 6.28, 6.28/100}]]
dataf = pd.read_csv(r'F:\dataexample\out01.csv')
x = list(dataf.loc[:, 'x'])

y = list(dataf.loc[:, 'y'])

plt.plot(x, y)
plt.show()
