# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: D_datascience-200430-DA
#     language: python
#     name: d_datascience-200430-da
# ---

# + [markdown] pycharm={"name": "#%% md\n"}
# # Crime Sampler Using Dataset From Chicago Police
# -

# # IMPORT LIBRARY

# + [markdown] pycharm={"name": "#%% md\n"}
# Import necessary library

# + pycharm={"name": "#%%\n"}
# Import the csv module
import csv

# Import the pendulum module for datetime manipulation
import pendulum

# Import Counter, defaultdict from collections module
from collections import Counter
from collections import defaultdict

# Import the datetime module
from datetime import datetime

# + [markdown] pycharm={"name": "#%% md\n"}
# Open Crime Sampler dataset using csv import

# + pycharm={"name": "#%%\n"}
# Create the file object: csvfile
csv_file = open('Crimes2018.csv','r')

# Create an empty list: crime_data
crime_data = []

# + [markdown] pycharm={"name": "#%% md\n"}
# Read crime_sampler.csv line by line, then convert it to crime_data list

# + pycharm={"name": "#%%\n"}
# Loop over a csv reader on the file object
for row in csv.reader(csv_file):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[2], row[5], row[7], row[8]))

# + pycharm={"name": "#%%\n"}
crime_data[0:3]

# + pycharm={"name": "#%%\n"}
# Remove the first element from crime_data
crime_data.pop(0)
# -

# Print crime_data for 10 first list

# + pycharm={"name": "#%%\n"}
# Print the first 10 records
print(crime_data[:10])

# + [markdown] pycharm={"name": "#%% md\n"}
# # CRIME BY MONTH

# + [markdown] pycharm={"name": "#%% md\n"}
# Find the Months with the Highest Number of Crimes

# + pycharm={"name": "#%%\n"}
# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# + pycharm={"name": "#%%\n"}
# Loop over the crime_data list
for date in crime_data:

    # Convert the first element of each item into a Python Datetime Object: date
    date = datetime.strptime(date[0], '%m/%d/%Y %I:%M:%S %p')

    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
# -

# Print top 3 month for crime

# + pycharm={"name": "#%%\n"}
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))

# + [markdown] pycharm={"name": "#%% md\n"}
# We can see that Month of August was the highest crime month followed by July and May.
# -

# Now time to flip our crime_data list into a dictionary
# keyed by month with a list of location values for each
# month, and filter down to the records for the year 2018

# + pycharm={"name": "#%%\n"}
# Create a dictionary that defaults to a list: locations_by_month
locations_by_month = defaultdict(list)

# + pycharm={"name": "#%%\n"}
# Loop over the crime_data list
for row in crime_data:
    # Convert the first element to a date object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')

    # If the year is 2018
    if date.year == 2018:
        # Set the dictionary key to the month and append the location (2nd element) to the values list
        locations_by_month[date.month].append(row[2])

# + pycharm={"name": "#%%\n"}
# Print the dictionary for Month January

print(locations_by_month[1])

# + [markdown] pycharm={"name": "#%% md\n"}
# Find the Most Common Crimes by Location Type by Month in 2018

# + pycharm={"name": "#%%\n"}
# Loop over the items from locations_by_month using tuple expansion of the month and locations
for month, locations in locations_by_month.items():
    # Make a Counter of the locations
    location_count = Counter(locations)
    # Print the month
    print(month)
    # Print the most common location
    print(location_count.most_common(5))
# -

# We can see that most common of crime occured was on the Street

# # CRIME BY DISTRIC

# Now we want to know crime by district

# + pycharm={"name": "#%%\n"}
# Create the file object: csvfile
csv_file = open('Crimes2018.csv','r')

# Create a dictionary that defaults to a list: crimes_by_district
crimes_by_district = defaultdict(list)
# -

# Read crime_sampler.csv line by line, then convert it to crime_by_district list

# + pycharm={"name": "#%%\n"}
# Loop over a DictReader of the CSV file
for row in csv.DictReader(csv_file):
    # Pop the district from each row: district
    district = row.pop('District')
    # Append the rest of the data to the list for proper district in crimes_by_district
    crimes_by_district[district].append(row)
# -

# for district, crimes in crimes_by_district.items():
#     # Print the district
#     print(district)
#
#     # Create an empty Counter object: year_count
#     year_count = Counter()
#
#     # Loop over the crimes:
#     for crime in crimes:
#         # If there was an arrest
#         if crime['Arrest'] == 'true':
#             # Convert the Date to a datetime and get the year
#             year = datetime.strptime(crime['Date'], '%m/%d/%Y %I:%M:%S %p').year
#             # Increment the Counter for the year
#             year_count[year] += 1
#
#     # Print the counter
#     print(year_count)

# # CRIME BY DISTRIC

# Now we want to know crime by district

# + pycharm={"name": "#%%\n"}
# Create the file object: csvfile
csv_file = open('Crimes2018.csv','r')

# Create a dictionary that defaults to a list: crimes_by_district
crimes_by_district = defaultdict(list)
# -

# Read crime_sampler.csv line by line, then convert it to crime_by_district list

# + pycharm={"name": "#%%\n"}
# Loop over a DictReader of the CSV file
for row in csv.DictReader(csv_file):
    # Pop the district from each row: district
    district = row.pop('District')
    # Append the rest of the data to the list for proper district in crimes_by_district
    crimes_by_district[district].append(row)

# + pycharm={"name": "#%%\n"}
for district, crimes in crimes_by_district.items():
    # Print the district
    print(district)

    # Create an empty Counter object: year_count
    year_count = Counter()

    # Loop over the crimes:
    for crime in crimes:
        # If there was an arrest
        if crime['Arrest'] == 'true':
            # Convert the Date to a datetime and get the year
            year = datetime.strptime(crime['Date'], '%m/%d/%Y %I:%M:%S %p').year
            # Increment the Counter for the year
            year_count[year] += 1

    # Print the counter
    print(year_count)

# + [markdown] pycharm={"name": "#%% md\n"}
# Can be seen that district '011' most crime this 2018 year
#
