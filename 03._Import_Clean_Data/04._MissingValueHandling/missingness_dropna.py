# %%

# Import library for file handling
import os

# %%

# Import library for data processing
from numpy.random import rand
import pandas as pd

#%%

# Import library for plotting
from matplotlib import pyplot as plt
import seaborn as sns

#%%

# Import library to analyze missing value
import missingno as msno

# %%


def fill_dummy_values(df, scaling_factor):
    # Create copy of dataframe
    df_dummy = df.copy(deep=True)
    # Iterate over each column
    for col in df_dummy:
        # Get column, column missing values and range
        col = df_dummy[col]
        col_null = col.isnull()
        num_nulls = col_null.sum()
        col_range = col.max() - col.min()
        # Shift and scale dummy values
        dummy_values = (rand(num_nulls) - 2)
        dummy_values = dummy_values * scaling_factor * col_range + col.min()
        # Return dummy values
        col[col_null] = dummy_values
    return df_dummy


# %%

# Import diabetes file as pandas DataFrame
diabetes = pd.read_csv(os.path.join('00._data', 'pima-indians-diabetes-data.csv'))

#%%

# Display head
print(diabetes.head())

#%%

diabetes_dummy = fill_dummy_values(diabetes, 0.075)
nullity = diabetes.Skin_Fold.isnull() + diabetes.BMI.isnull()

#%%

diabetes_dummy.plot(x='Skin_Fold', y='BMI', kind='scatter', alpha=0.5, c=nullity, cmap='rainbow')
plt.show()

#%%

# Visualize the missingness of diabetes prior to dropping missing values
msno.matrix(diabetes)
plt.show()

#%%
# Print the number of missing values in Glucose
print(diabetes['Glucose'].isnull().sum())

#%%

# Drop rows where 'Glucose' has a missing value
diabetes.dropna(subset=['Glucose'], how='any', inplace=True)

#%%
# Visualize the missingness of diabetes after dropping missing values
msno.matrix(diabetes)
plt.show()

#%%

# Visualize the correlation of missingness between variables
msno.heatmap(diabetes)

# Show heatmap
plt.show()

#%%
# Drop rows where 'BMI' has a missing value
diabetes.dropna(subset=['BMI'], how='all', inplace=True)

#%%

msno.matrix(diabetes)
plt.show()

#%%

print(diabetes.info())
