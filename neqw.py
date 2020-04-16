import numpy as np

a = np.arange(24).reshape(4, 6)
print(a)
print('#'*50)
# 切片:先写个逗号，逗号前放行，后放列
print(a[0, :])
print('#' * 50)
print(a[:, 0])
print('#' * 50)
print(a[0:3, :])
print('#' * 50)
print(a[(0, 3), (1, 2)])
print('#' * 50)
print(a[(0, 1, 3), (1, 2, 2)])
print('#' * 50)
print(a[0:3, 1:2])
print('#' * 50)

a[a > 20] = 1
print(a)
print('#' * 50)

#! nan是浮点类型

t = np.arange(12).reshape(3, 4)
print(t)
t = t.astype(float)
t[2, 2] = np.nan
print(t)
#! 
#! 行列的交换
print('*' * 50)
t[[1, 2], :] = t[[2, 1], :]
print(t)

#? 交换两个数
print('*' * 50)
a, b = 1, 2
print(a, b)
print('------')
a, b = b, a
print(a, b)
