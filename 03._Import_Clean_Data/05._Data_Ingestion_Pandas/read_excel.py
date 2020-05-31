#%%
import os
import pandas as pd
import matplotlib.pyplot as plt

#%%

excel_file = os.path.join('00._data', "fcc-new-coder-survey.xlsx")

# Create string of lettered columns to load
col_string = 'AD, AW:BA'

#%%

survey_responses = pd.read_excel(excel_file)
print(survey_responses.head())

# can seen from result that unnecessary meta data imported, next we need to skip it.

#%%

# Load data with skiprows and usecols set
survey_responses = pd.read_excel(excel_file,
                                 skiprows=2,
                                 usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)

#%%

# Getting data from multiple worksheets, now read sheet 1 ('2017')

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel(excel_file,
                               sheet_name=1,
                               skiprows=2,
                               usecols=col_string)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

#%%

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel(excel_file,
                               sheet_name='2017',
                               skiprows=2,
                               usecols=col_string)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

#%%

# Load both the 2016 and 2017 sheets by name
all_survey_data_name = pd.read_excel(excel_file,
                                     sheet_name=['2016', '2017'],
                                     skiprows=2,
                                     usecols=col_string)

# View the data type of all_survey_data
print(type(all_survey_data_name))

#%%

# Load both the 2016 and 2017 sheets by location and name
all_survey_data_locname = pd.read_excel(excel_file,
                                        sheet_name=[0, '2017'],
                                        skiprows=2,
                                        usecols=col_string)

# View the data type of all_survey_data
print(type(all_survey_data_locname))

#%%

# Load all sheets in the Excel file
all_survey_data = pd.read_excel(excel_file,
                                sheet_name=None,
                                skiprows=2)

# View the data type of all_survey_data
print(type(all_survey_data))

#%%

# Create an empty data frame
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for dfx in all_survey_data.values():
    # Print the number of rows being added
    print("Adding {} rows".format(dfx.shape[0]))
    # Append df to all_responses, assign result
    all_responses = all_responses.append(dfx)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

#%%

# Method 2, if all columns have same name, and all sheet
# have same column

df = pd.concat(pd.read_excel(excel_file,
                             sheet_name=None,
                             skiprows=2),
               ignore_index=True)

# Graph employment statuses in sample
countsz = df.groupby("EmploymentStatus").EmploymentStatus.count()
countsz.plot.barh()
plt.show()
