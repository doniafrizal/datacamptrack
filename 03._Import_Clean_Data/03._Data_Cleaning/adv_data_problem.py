#%%
import os
import pandas as pd
import numpy as np
import random
import datetime as dt
import missingno as msno
import matplotlib.pyplot as plt

# %%

# Member Constraint

# Air Lines data frame
banking = pd.read_csv(os.path.join('00._data', 'banking_dirty.csv'))

#%%
# Add new data to DataFrame for Currency
banking['acct_cur'] = [random.sample(['dollar', 'euro'], 1)[0] for i in range(len(banking[:]))]

#%%

# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Print unique values of acct_cur
assert banking['acct_cur'].unique() == 'dollar'

#%%

# Print the header of account_opend
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format=True,
                                           # Return missing value for error
                                           errors='coerce')

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])

#%%

# Cross validation

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

#%%

# Convert Colum Birthdate to datetime data type
banking['birth_date'] = banking['birth_date'].astype('datetime64[ns]')

#%%

# Store today's date and find ages
today = dt.datetime.today()
ages_manual = today.year - banking['birth_date'].dt.year

#%%
# Find rows where age column == ages_manual
age_equ = banking['Age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])

#%%

# Simulate missing data in inv_amount column
missing_inv_amount = [4, 14, 17, 18, 35, 40, 46, 54, 59, 82, 88, 93, 94]
banking.loc[missing_inv_amount, 'inv_amount'] = np.nan
print(banking.loc[missing_inv_amount, 'inv_amount'])

#%%

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

#%%

print(missing_investors[['Age', 'inv_amount']])

#%%

missing_cust_id = [13, 14, 24, 25, 31, 63, 72, 78, 96]

#%%

# Simulate missing data in cust_id column
banking.loc[missing_cust_id, 'cust_id'] = np.nan
print(banking.loc[missing_cust_id, 'cust_id'])

#%%

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset=['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())
