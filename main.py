import requests
from bs4 import BeautifulSoup
url= "https://akshatchatterjee.tk"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML (HTMLparser and beautifulSoup)
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML tree traversal
# title = soup.title
# # Commonly used objects- Tag, 
# print(type(title))
# # NavigableString,
# print(type(title.string)) 
# # BeautifulSoup,
# print(type(soup)) 
# Comment

title = soup.title

# get all para tags

paras = soup.find_all('p')
print(paras)

# print(title)
# Step 4: Start... many methods!


