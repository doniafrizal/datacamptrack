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

# Getting data from multiple worksheets, now read sheet 1 ('2017')

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel(os.path.join('00._data', 'fcc-new-coder-survey.xlsx'),
                               sheet_name=1,
                               skiprows=2,
                               usecols=col_string)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

#%%

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel(os.path.join('00._data', 'fcc-new-coder-survey.xlsx'),
                               sheet_name='2017',
                               skiprows=2,
                               usecols=col_string)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()
