import requests
from bs4 import BeautifulSoup

website = 'http://quotes.toscrape.com'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

align = soup.find_all('div', class_='quote')
# print(align[0].text)


all_quotes = soup.find_all('span', class_='text')
# print(all_quotes)
# quotes and put them in a list
all_quotes = soup.find_all('span', class_='text')


for quote in all_quotes:
    print(quote.text)
#Use list indexing to select the second quote.
# [1] is the second item.
second_quote_tag = all_quotes[1]

# Extract just the text (without the HTML tags)
print(second_quote_tag.text)

# authors
all_authors = soup.find_all('small', class_='author')
print(all_authors[0].text)

for author in all_authors:
    print(author.text)
