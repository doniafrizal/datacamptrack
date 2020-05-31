# %%

# Import library for file handling
import os

# %%

# Import library for data processing
from numpy.random import rand
import pandas as pd
import numpy as np
from fancyimpute import KNN
from fancyimpute import IterativeImputer
from sklearn.preprocessing import OrdinalEncoder

#%%

# Import library for plotting
from matplotlib import pyplot as plt

# %%

# Import userprofile.csv file as pandas DataFrame
users = pd.read_csv(os.path.join('00._data', 'userprofile.csv'))

#%%

# Display head
print(users.info())
print(users.isnull().sum())

#%%

# Create Ordinal Encoder
ambience_ord_enc = OrdinalEncoder()
# Select non-null values in ambience
ambience = users['ambience']
ambience_not_null = ambience[ambience.notnull()]
reshaped_vals = ambience_not_null.values.reshape(-1, 1)
# Encode the non-null values of ambience
encoded_vals = ambience_ord_enc.fit_transform(reshaped_vals)
# Replace the ambience column with ordinal values
users.loc[ambience.notnull(), 'ambience'] = np.squeeze(encoded_vals)


#%%

# Create an empty dictionary ordinal_enc_dict
ordinal_enc_dict = {}

for col_name in users:
    # Create Ordinal encoder for col
    ordinal_enc_dict[col_name] = OrdinalEncoder()
    col = users[col_name]

    # Select non-null values of col
    col_not_null = col[col.notnull()]
    reshaped_vals = col_not_null.values.reshape(-1, 1)
    encoded_vals = ordinal_enc_dict[col_name].fit_transform(reshaped_vals)

    # Store the values to non-null values of the column in users
    users.loc[col.notnull(), col_name] = np.squeeze(encoded_vals)

#%%

# Create KNN imputer
KNN_imputer = KNN()

# Impute and round the users DataFrame
users.iloc[:, :] = np.round(KNN_imputer.fit_transform(users))

# Loop over the column names in users
for col_name in users:
    # Reshape the data
    reshaped = users[col_name].values.reshape(-1, 1)

    # Perform inverse transform of the ordinally encoded columns
    users[col_name] = ordinal_enc_dict[col_name].inverse_transform(reshaped)