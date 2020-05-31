#%%
import os
import pandas as pd
import random
from random import randrange
from datetime import timedelta
from datetime import datetime

#%%

ride_sharing = pd.read_csv(os.path.join('00._data', 'ride_sharing_new.csv'))

# ride_sharing.columns = ride_sharing.columns.str.replace(' ', '_')

#%%

# Print df head
print(ride_sharing.head())

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

#%%

# Data Type Constraint

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

#%%

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

#%%

# Print new summary statistics
print(ride_sharing['user_type_cat'].describe())

#%% md
# Summing Strings and concatenating numbers

#%%

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration
print(ride_sharing[['duration', 'duration_trim', 'duration_time']])
print(ride_sharing['duration_time'].mean())

#%%

# Add new data to DataFrame for Tire Size

ride_sharing['tire_sizes'] = [random.sample([25, 27, 29], 1)[0] for _ in range(len(ride_sharing[:]))]

#%%

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Convert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Make sure data type
assert ride_sharing['tire_sizes'].dtype == 'category'

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

#%%


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

#%%

# Add new data to DataFrame for Ride Date


d1 = datetime.strptime('1/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

#%%
ride_sharing['ride_date'] = [random_date(d1, d2) for _ in range(len(ride_sharing[:]))]

#%%

# Save today's date
today = datetime.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

#%%

ride_sharing['ride_id'] = [random.randint(0, len(ride_sharing[:])) for _ in range(len(ride_sharing[:]))]

#%%

# Find duplicates
duplicates = ride_sharing.duplicated('ride_id', keep=False)

#%%
# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']])

#%%

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

#%%
# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

#%%

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()
#%%

# Find duplicated values again
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
print(duplicates)

#%%

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
