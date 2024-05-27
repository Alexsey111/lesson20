import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)
plt.title('Диаграмма рассеяния')
plt.xlabel('ось х')
plt.ylabel('ось у')
plt.show()