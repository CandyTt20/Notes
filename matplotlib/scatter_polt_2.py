from matplotlib import pyplot as plt

x = ['A', 'B', 'C']
y = [12, 7, 3]

plt.barh(range(len(x)), y, height=0.1)
plt.yticks(range(len(x)), x)
plt.show()
