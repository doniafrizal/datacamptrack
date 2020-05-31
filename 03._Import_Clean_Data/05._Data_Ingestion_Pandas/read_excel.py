#%%
import os
import pandas as pd
import matplotlib.pyplot as plt

#%%

survey_responses = pd.read_excel(os.path.join('00._data', 'fcc-new-coder-survey.xlsx'))
print(survey_responses.head())

# can seen from result that unnecessary meta data imported, next we need to skip it.

#%%

# Create string of lettered columns to load
col_string = 'AD, AW:BA'

# Load data with skiprows and usecols set
survey_responses = pd.read_excel(os.path.join('00._data', 'fcc-new-coder-survey.xlsx'),
                                 skiprows=2,
                                 usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)

#%%

# Getting data from multiple worksheets


