from matplotlib import pyplot as plt

x = ['A', 'B', 'C']
y = [12, 7, 3]

plt.bar(range(len(x)), y, width=0.1)
plt.xticks(range(len(x)), x)
plt.show()
