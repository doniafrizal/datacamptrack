#%%

import os
import pandas as pd
import matplotlib.pyplot as plt

#%%

data = pd.read_csv(os.path.join('00._data', 'vt_tax_data_2016.csv'))
data.head()

#%%

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()

#%%

# Import selected columns only

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create data frame from csv using only selected columns
data = pd.read_csv(os.path.join('00._data', 'vt_tax_data_2016.csv'), usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

#%%

# Create data frame of next 500 rows with labeled columns
vt_data_first500 = pd.read_csv(os.path.join('00._data', 'vt_tax_data_2016.csv'),
                               nrows=500)

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())

#%%

# Create data frame of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv(os.path.join('00._data', 'vt_tax_data_2016.csv'),
                              nrows=500,
                              skiprows=500,
                              header=None,
                              names=list(vt_data_first500))

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

#%%

# To check data type

# Load csv with no additional arguments
data = pd.read_csv(os.path.join('00._data', 'vt_tax_data_2016.csv'))

# Print the data types
print(data.dtypes)

# from result, agi_stub shall be category type, while zipcode must be str type.

#%%

# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub': 'category',
              'zipcode': str}

# Load csv using dtype to set correct data types
data = pd.read_csv(os.path.join('00._data', 'vt_tax_data_2016.csv'), dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())

#%%

# create NA for null values

# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode': 0}

# Load csv using na_values keyword argument
data = pd.read_csv(os.path.join('00._data', 'vt_tax_data_2016.csv'),
                   dtype=data_types,
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])
