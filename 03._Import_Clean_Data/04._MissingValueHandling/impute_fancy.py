# %%

# Import library for file handling
import os

# %%

# Import library for data processing
from numpy.random import rand
import pandas as pd
from fancyimpute import KNN
from fancyimpute import IterativeImputer

#%%

# Import library for plotting
from matplotlib import pyplot as plt

# %%

# Import diabetes file as pandas DataFrame
diabetes = pd.read_csv(os.path.join('00._data', 'pima-indians-diabetes-data.csv'))

#%%

# Display head
print(diabetes.head())

#%%

knn_imputer = KNN()
diabetes_knn = diabetes.copy(deep=True)

print(diabetes_knn.isnull().sum())

diabetes_knn.iloc[:, :] = knn_imputer.fit_transform(diabetes_knn)

print(diabetes_knn.isnull().sum())

#%%

MICE_imputer = IterativeImputer()
diabetes_MICE = diabetes.copy(deep=True)
diabetes_MICE.iloc[:, :] = MICE_imputer.fit_transform(diabetes_MICE)

#%%
print(diabetes_MICE.isnull().sum())
