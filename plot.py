import numpy as np
import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        pass


a = np.random.normal(200000, 25000, 5000)
plt.hist(a, 50)
plt.show()
