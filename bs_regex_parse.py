from bs4 import BeautifulSoup as Soup
import re

string = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
match = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)

html = Soup(string, 'html.parser')    
bsm=  [a['href'] for a in html.find_all('a')]
match2 = re.findall('"(http.*.*)"',string)

print(match)
print(match2)
print(bsm)
