# pagination is simply going to next page for data

import requests
from bs4 import BeautifulSoup
import time

base_url = 'http://quotes.toscrape.com'

current_relative_url = '/tag/inspirational/'

next_page_exists = True

while next_page_exists:

    #  base URL and the current page together
    full_url = base_url + current_relative_url
    print(f"\n--- Loading Page: {full_url} ---")

    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # getting data
    all_quotes = soup.find_all('span', class_='text')
    for quote in all_quotes:
        print(quote.text)

    # On website, the next button is inside an <li> tag with class="next"
    next_button_box = soup.find('li', class_='next')

    if next_button_box:
        # If the box exists, find the <a> tag inside it and get href!
        next_link = next_button_box.find('a')['href']

        # Update the url so the NEXT loop goes to the new page
        current_relative_url = next_link

        print("-> Next button found! going to page...")
        time.sleep(1) 
      
    else:
        print("-> No 'Next' button found. We are in final page!")
        next_page_exists = False

print("\nAll pages scraped successfully.")
