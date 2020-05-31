#%%

from urllib.request import urlopen, Request
import requests

#%%
url = "https://www.wikipedia.org/"
request = Request(url)
response = urlopen(request)
html = response.read()
print(html)
response.close()

#%%

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)
