

import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the parent quote boxes
quote_boxes = soup.find_all('div', class_='quote')

for box in quote_boxes:
    quote = box.find('span', class_='text').text
    author = box.find('small', class_='author').text

    # Find the <a> tag for the "about" link inside this box
    about_tag = box.find('a', text='(about)')
    relative_link = about_tag['href']  # Gives us something /author/Albert-Einstein

    # Combine base URL + relative link to get the absolute URL
    author_full_url = base_url + relative_link

    #  Making new request to the author's private detail page!
    author_response = requests.get(author_full_url)
    author_soup = BeautifulSoup(author_response.text, 'html.parser')

    # getting the birthdate from the inner author page
    birth_date = author_soup.find('span', class_='author-born-date').text

    # Now we got linked data across two different pages!
    print(f"Author: {author} , Born: {birth_date} , Quote: {quote}")
