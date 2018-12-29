from urllib.request import urlretrieve
url = "https://nrogg.com"
urlretrieve(url,'file.csv')

from urllib.request import urlopen, Request
url = "https://www.wikipedia.org"
request = Request(url)
response = urlopen(request)
html = response.read() #To read the response and store in a file
response.close() #To close the link

#Shortcut for above steps is to use the requests package
import requests
url = "https://www.wikipedia.org"
r = requests.get(url) #To activate the request
text = r.text #To convert html file into text file

from bs4 import BeautifulSoup
import requests
url = "https://www.wikipedia.org"
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.prettify()) #Prints well indendeted HTML files
print(soup.title()) #Prints the title of the HTML file
print(soup.get_text()) #Extracts the text from the HTML file
for link in soup.find_all('a'):
    print(link.get('href')) #To print all the hyperlinks in the html file
with open("a_movie.json") as json_file:
    json_data = json.load(json_file) #imports as a list

r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key + ' ', value)
#An API is a bunch of codes that allows two software programs to interact with each other
