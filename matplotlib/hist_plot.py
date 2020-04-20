from matplotlib import pyplot as plt
import random
a = [random.randint(0, 10) for i in range(0, 100)]
plt.hist(a, bins=20)
plt.show()
