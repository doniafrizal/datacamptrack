#%%
# Import packages
import requests
from bs4 import BeautifulSoup
import json
import os
import tweepy
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt

#%%

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

#%%

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

#%%

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)

#%%

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))

#%%

with open(os.path.join('00._data', 'Film.JSON'), 'r') as json_file:
    json_data = json.load(json_file)

print(type(json_data))

#%%

for key, value in json_data.items():
    print(key + ':', value)

#%%

# Working with OMDB API

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)

#%%

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

#%%

# Working with Wikipedia API

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

#%%

# Store OAuth authentication credentials in relevant variables
access_token = "42358143-SzNG3J8cjev100TOgw7sLEz0Zckj7r6fJdYicOYqQ"
access_token_secret = "vAfCZw3SLfT0UrgIDEjkowHqx6s1b7PEf8fSJKzeYxDV7"
consumer_key = "Nel2hOcYBwqJMcX5aSgFwjxxV"
consumer_secret = "KJ2u1T5cU40FusrbPXHPQfzxyn1YPi9OzXlRv46crZzr1ktyP1"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#%%


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open(os.path.join('00._data', 'tweets.txt'), 'w')

    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

#%%


# Create Streaming object and authenticate
listen = MyStreamListener()
stream = tweepy.Stream(auth, listen)
# This line filters Twitter Streams to capture data by keywords:
stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])

#%%

# String of path to file: tweets_data_path
tweets_data_path = os.path.join('00._data', 'tweets.txt')
# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

#%%

# Twitter Data to DataFrame


# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())

#%%

print(df)

#%%


def word_in_text(word, text):
    """
    to analyze whether a 'word' in first argument occurs within 2nd argument 'text'
    :param word:
    :param text:
    :return:
    """
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

#%%


# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

#%%

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot the bar chart
ax = sns.barplot(cd,[clinton, trump, sanders, cruz] )
ax.set(ylabel="count")
plt.show()
