import requests
from bs4 import BeautifulSoup
import csv

website = 'http://quotes.toscrape.com'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'html.parser')

# Open new CSV file to write our data
# encoding='utf-8' ensures special characters (like quotes/emojis) save correctly.
with open('my_first_dataset.csv', 'w', newline='', encoding='utf-8') as file:
    
    writer = csv.writer(file)


    
    writer.writerow(['Quote', 'Author','Tags'])

    
    all_quote_boxes = soup.find_all('div', class_='quote')

    
    for box in all_quote_boxes:
        
        quote_text = box.find('span', class_='text').text
        author_name = box.find('small', class_='author').text
        quote_tags = box.find('meta', class_='keywords')['content']

        writer.writerow([quote_text, author_name,quote_tags])

print("Data successfully saved to dataset.csv")
