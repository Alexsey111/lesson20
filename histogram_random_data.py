import numpy as np
import matplotlib.pyplot as plt

mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов

data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=30)
plt.title('Гистограмма для случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.show()