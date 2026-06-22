import requests
from bs4 import BeautifulSoup
base_url = 'http://quotes.toscrape.com/'
current_url = 'http://quotes.toscrape.com/page/1/'

page_number = 1

while current_url:
    print(f'current_page_number:{page_number}')

    response = requests.get(current_url)
    result = response.text
    soup = BeautifulSoup(result, 'html.parser')

    quote_boxes = soup.find_all('div', class_='quote')
    # print(quote_boxes)
    # quote boxes gives everything in list......
    for quote in quote_boxes:
        quote_text = quote.find('span', class_='text')
        quote_author = quote.find('small', class_='author')
        if page_number == 1:
            print(quote_text.text)
        elif page_number == 2:
            print(f'{quote_text.text},{quote_author.text}')
        elif page_number == 3:
            level2_url = quote.find('a', string='(about)')
            about_url = level2_url['href']
            lvl2_url = base_url + about_url
            level2_response = requests.get(lvl2_url)
            level2_soup = BeautifulSoup(level2_response.text, 'html.parser')
            author_birth = level2_soup.find('span', class_='author-born-date')
            print(f'{quote_text.text},{quote_author.text},author_birth:{author_birth.text}')

            # print(current_url)
            # print(new_url)

    next_button = soup.find('li', class_='next')
    if next_button:
        new_url = next_button.find('a')['href']
        current_url = base_url + new_url
        page_number += 1

    else:
        current_url = None
