import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=50)
plt.show()
