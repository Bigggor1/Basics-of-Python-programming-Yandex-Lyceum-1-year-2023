import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = pd.read_csv('penguins.csv')

X = data.drop(columns=['flipper_length_mm'])
X['sex'] = X['sex'].replace({'MALE': 0, 'FEMALE': 1})
X['sex'] = X['sex'].fillna(round(X['sex'].mean()))
X = pd.get_dummies(X, columns=['island', 'species'])

y = data['flipper_length_mm']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_predict = lr.predict(X_test)

MAE = mean_absolute_error(y_test, y_predict)
MSE = mean_squared_error(y_test, y_predict)
print(MAE, MSE)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection='3d')

# визуализируем точки обучающей выборки
x_points = data['body_mass_g']
y_points = data['bill_length_mm']
z_points = data['flipper_length_mm']

ax.scatter(x_points, y_points, z_points)

ax.set_xlabel('масса тела');
ax.set_ylabel('длина клюва');
ax.set_zlabel('длина плавника');

plt.show()