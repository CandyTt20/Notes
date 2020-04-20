from matplotlib import pyplot as plt

age = range(11, 31)
num = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
num2 = [1, 2, 0, 4, 4, 2, 0, 1, 2, 5, 2, 1, 3, 2, 1, 1, 5, 6, 1, 4]

plt.xticks(age)
plt.yticks(range(min(num), max(num)))

# !设置网格
plt.grid(alpha=0.1)


plt.xlabel('Your Age')
plt.ylabel('Your Friends')
plt.title('Friends as a plot of age')

# !更改坐标轴粗细
ax = plt.gca()  # 获取坐标轴句柄
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)

# !label添加图例
plt.plot(age, num, label='a', color='r', linestyle='--', linewidth=2)
plt.plot(age, num2, label='b', color='g')

# 显示图例
plt.legend()

plt.show()
