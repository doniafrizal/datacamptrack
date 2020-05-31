# %%
import os
import pandas as pd
import numpy as np

# %%

# Member Constraint

# Air Lines data frame
airlines = pd.read_csv(os.path.join('00._data', 'airlines_final.csv'))

# %%

# Create Categories DataFrame

category = {
    'cleanliness': ['Clean', 'Average', 'Somewhat clean', 'Somewhat dirty', 'Dirty'],
    'safety': ['Neutral', 'Very safe', 'Somewhat safe', 'Very unsafe', 'Somewhat unsafe'],
    'satisfaction': ['Very satisfied', 'Neutral', 'Somewhat satisfied',
                     'Somewhat unsatisfied', 'Very unsatisfied']
}
categories = pd.DataFrame(category, dtype="category")

print(categories)

# %%

# Finding inconsistent category

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(),
      "\n Cleanliness category :", *categories['cleanliness'])
print('Safety: ', airlines['safety'].unique(),
      "\n Safety Category: ", *categories['safety'])
print('Satisfaction: ', airlines['satisfaction'].unique(),
      "\n Satisfaction Category: ", *categories['satisfaction'])

# We can see that cleanliness have inconsistency category, it have 'Unacceptable' category

# %%

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])

# %%

# Categorical problem:
# a. whitespace
# b. inconsistency
# c. create new category
# d. remapping

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# %%


# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur': 'europe'})

# %%

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# %%

# Verify changes have been effected
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# %%

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# %%

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins=label_ranges,
                               labels=label_names)

# %%

# Create mappings and replace
mappings = {'Monday': 'weekday', 'Tuesday': 'weekday', 'Wednesday': 'weekday',
            'Thursday': 'weekday', 'Friday': 'weekday',
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)
airlines['day_week'] = airlines['day_week'].astype('category')
# %%

print(airlines['wait_type'].unique())
print(airlines['day_week'].unique())

# %%

# Cleaning Text Data

#%%

# Update airlines DataFrame with Name

full_name = pd.read_csv(os.path.join('00._data', 'fullnames.csv'), sep=',', usecols=['full_name'])
airlines['full_name'] = full_name

#%%

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Dr.', "")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Mr.', "")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Miss', "")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Ms.', "")

# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

#%%

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])