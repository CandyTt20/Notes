import numpy as np
import random
# 创建数组
x = np.array([1, 2, 3], dtype=float)
print(x)

x1 = np.arange(10)
print(x1)

# 数组存放数据的类型
print(x.dtype)
#! 调整数据类型
x.astype('int8')
print(x)
print('----------------------------------------')
x2 = np.array([random.random() for i in range(10)])
print(x2)
print('----------------------------------------')
x3 = np.round(x2, 2)
print(x3)
print('----------------------------------------')

print(x2.shape)
print('----------------------------------------')

# TODO 广播机制 
# * NaN = not a number