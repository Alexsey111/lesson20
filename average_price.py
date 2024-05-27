import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
data = pd.read_csv('prices.csv')

# Вычисление средней цены
average_price = data['Price'].mean()
print("Средняя цена на диваны:", round(average_price, 2), "руб.")

# Построение гистограммы цен
plt.hist(data['Price'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Цена, руб.')
plt.ylabel('Частота')
plt.title('Гистограмма цен на диваны')
plt.grid(True)
plt.show()
