import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import accuracy_score, make_scorer, mean_squared_error
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler

melb_data = pd.read_csv('melb_data.csv')
data_hw = pd.read_csv('hw_25000.csv')
data_ex = pd.read_csv('https://ai-academy.ru/upload/csv/Restaurant.csv')
titanic_data = pd.read_csv('titanic.csv', index_col='PassengerId')
telecom_data = pd.read_csv('telecom_churn.csv')
seterra_data = pd.read_csv('seterra.csv')

y = melb_data['Price']
x = melb_data.drop(
    columns=['Price', 'Suburb', 'Address', 'Method', 'SellerG', 'Date', 'Postcode', 'BuildingArea', 'Lattitude', 'Longtitude',
             'Regionname', 'CouncilArea'])

x['Rooms'] = x['Rooms'].astype(float)
x['Car'] = x['Car'].fillna(x['Car'].mean())
x['YearBuilt'] = x['YearBuilt'].fillna(x['YearBuilt'].mean())
x = pd.get_dummies(x, columns=['Type'])

scaler = StandardScaler()
x = scaler.fit_transform(x)

knn = KNeighborsRegressor(5)

scorer = make_scorer(lambda y_true, y_pred: mean_squared_error(y_true, y_pred),
                     greater_is_better=False)
errors = cross_val_score(knn, x, y, cv=5, scoring=scorer)

print()
print('Metrics')
print(errors)
print('RMSE=', np.mean(-errors) ** 0.5)