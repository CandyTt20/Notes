import matplotlib
from matplotlib import pyplot as plt
import random
import io
import sys
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# 绘图中设置中文字体显示以及粗细MicroSoft YaHei
font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': '10'}
matplotlib.rc("font", **font)


# 设置画图大小
plt.figure(figsize=(50, 10), dpi=80)
t = [random.randint(20, 35) for i in range(0, 120, 10)]
x = range(0, 120, 10)

# 坐标轴显示字符串
_x = x
_x_tick_1 = ['10点{}分'.format(i) for i in range(10, 60, 10)]
_x_tick_2 = ['11点{}分'.format(i) for i in range(0, 60, 10)]
for i in _x_tick_2:
    _x_tick_1.append(i)
_x_tick_1.append('12点0分')
plt.xticks(_x, _x_tick_1, rotation=45)  # 字符要和数字一一对应,rotation->旋转字符

# 设置描述信息
plt.xlabel('时间')
plt.ylabel('温度（摄氏度）')
plt.title('温度变化图')

# 画图
plt.plot(x, t)
plt.show()
