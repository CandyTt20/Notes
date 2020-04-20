import numpy as np
import pandas as pd
x = pd.Series(np.arange(5), index=list('abcde'))
print(x)
print("*" * 20)

a = pd.Series({"a": 1, "b": 2})
print(a.dtype)
a = a.astype(float)
print("*" * 20)
print(a)
print("*" * 20)
print(x)
print(x[[0,2]])
