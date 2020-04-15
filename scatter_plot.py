from matplotlib import pyplot as plt
import random

a = [random.randint(10, 20) for i in range(0, 31)]
b = [random.randint(10, 20) for i in range(0, 31)]
# print(a)
plt.figure(figsize=(80, 20), dpi=70)

x_a = range(0, 31)
x_b = range(42, 73)

x_ticks = ['Mar.{}'.format(i + 1) for i in range(0, 31)]
y_ticks = ['Otc.{}'.format(i-41) for i in x_b]
_ticks = x_ticks + y_ticks

plt.xticks(list(x_a)[::3]+list(x_b)[::3], _ticks[::3], rotation=45)
plt.xlabel('Days')
#! 绘制散点图
plt.scatter(x_a, a, color='r',label = 'March')
plt.scatter(x_b, b,label = 'October')
plt.legend()
plt.show()

