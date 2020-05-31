#%%
import os
import pandas as pd
import random
from fuzzywuzzy import process
import recordlinkage

# %%

# Member Constraint

# Air Lines data frame
restaurants = pd.read_csv(os.path.join('00._data', 'restaurants_L2_dirty.csv'))
restaurants_new = pd.read_csv(os.path.join('00._data', 'restaurants_L2.csv'))


#%%

# Replace cuisine type
cuisine = ['america', 'merican', 'amurican', 'americen', 'americann',
           'asiane', 'itali', 'asiann', 'murican', 'italien', 'italian',
           'asiat', 'american', 'americano', 'italiann', 'ameerican',
           'asianne', 'italiano', 'americin', 'ammericann', 'amerycan',
           'aamerican', 'ameriican', 'italiaan', 'asiian', 'asiaan',
           'amerrican', 'ameerrican', 'ammereican', 'asian', 'italianne',
           'italiian', 'itallian']

restaurants['type'] = [random.sample(cuisine, 1)[0] for i in range(len(restaurants[:]))]

#%%

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants.type.unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit=len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit=len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit=len(unique_types)))

# Best cut-off for string matching is similarity to 80

#%%

# create categories
categories = pd.DataFrame({'cuisine_type': ['asian', 'american', 'italian']}, dtype='category')

#%%

# For each correct cuisine_type in categories

# process.extract(), the output is a list of tuples where each of tuple is as such:
# (closest match, similarity score, index of match)

for cuisine in categories['cuisine_type']:
    # Find matches in cuisine_type of restaurants
    matches = process.extract(cuisine, restaurants['type'],
                              limit=restaurants.shape[0])

    # For each possible_match with similarity score >= 80
    for possible_match in matches:
        if possible_match[1] >= 80:
            # Find matching cuisine type
            matching_cuisine = restaurants['type'] == possible_match[0]
            restaurants.loc[matching_cuisine, 'type'] = cuisine

# Print unique values to confirm mapping
print(restaurants['type'].unique())

# Can seen that restaurants['type'] consist only 3 type of cuisine.

#%%

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)

#%%
# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types -
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('type', 'type', label='type')

# Find similar matches of rest_name
comp_cl.string('name', 'name', label='name', threshold=0.8)

#%%

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

#%%

# to make sure we found duplicated row
# we need to set n = 3 as we need to find match between 3 column (name, city, type)
n = 3

matches = potential_matches[potential_matches.sum(axis=1) >= n]
print(matches)

#%%

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis = 1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
