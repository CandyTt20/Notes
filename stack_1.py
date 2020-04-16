import numpy as np
x_1 = np.arange(12).reshape(3, 4)
x_2 = np.arange(12, 24).reshape(3, 4)
# print(x_1, x_2)
# t_1 = np.arange(3).reshape(3, 1)

t_1 = np.array([0 for i in range(x_1.shape[0])]).reshape(3, 1)
y_1 = np.hstack((x_1, t_1))
# print(y_1)

#! 1. 全为0全为1的数值
#! 2. 最大值的位置：np.argmax(t,axis=0)

# ? numpy中随机数组：产生个2行3列的数组，每个元素值在0，10之间
p = np.random.randint(0, 10, (2, 3))
print(p)
