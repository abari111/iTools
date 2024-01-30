import requests
from bs4 import BeautifulSoup

# Make a request to the web page
response = requests.get('https://www.geeksforgeeks.org/computational-graphs-in-deep-learning/')

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Print the rendered HTML content
print(soup.prettify())