import numpy as np
import pandas as pd
t = pd.read_csv(r'F:\python_note\dogNames2.csv')
# print(t[20:50])
# t1 = pd.DataFrame(np.arange(12).reshape(
# 3, 4), index=list('abc'), columns=list('wxyz'))
# t1.info()
t = t.sort_values(by="Count_AnimalName", ascending=False)
print(t)
