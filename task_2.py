import numpy as np
import matplotlib.pyplot as plt

random_array_1 = np.random.rand(5)
print(random_array_1)

random_array_2 = np.random.rand(5)
print(random_array_2)

plt.scatter(random_array_1, random_array_2)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("диаграмма рассеяния для двух наборов случайных данных")

plt.show()
