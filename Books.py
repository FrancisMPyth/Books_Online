import requests
import csv
from bs4 import BeautifulSoup

# URL de la page produit
url = 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'
# Envoie de la requête HTTP
response = requests.get(url)
# Vérification du code d'état HTTP
if response.status_code == 200:
    # Extraction du contenu HTML
    html = response.content
    # Initialisation de BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # verification  des informations demandées
    # product_page_url
    print("product_page_url" , response.url)
    # UPC
    upc = soup.find('td').text
    # Afficher UPC
    print("universal_product_code_(upc)" , upc)
    # Trouver la balise du titre
    title = soup.find('h1').text
    # Extraire le titre de la balise
    title_text = title
    # Afficher le titre
    print("title", title)
    # Exraire les prix
    excl_tax_price = soup.find('th', string='Price (excl. tax)').find_next_sibling('td').text
    incl_tax_price = soup.find('th', string='Price (incl. tax)').find_next_sibling('td').text
    # Imprimer les prix
    print("price_including_tax", incl_tax_price)
    print("price_excluding_tax:", excl_tax_price)
    # Quantité
    number_available = soup.find('p', {'class': 'instock availability'}).text.strip()
    print('Number_available', number_available)
    # product_description
    product_description = soup.find('div', {'id': 'product_description'}).find_next('p').text.strip()
    print('Product_description', product_description)
    # Catégorie
    category = soup.select('ul.breadcrumb > li:nth-of-type(3) > a')[0].text
    print('Category', category)
    # Review_rating
    review_rating = soup.select('div.product_main > p.star-rating')[0].get('class')[1]
    print('Review rating', review_rating)
    # image_url
    image_url = soup.find('div', {'id': 'product_gallery'}).find('img').get('src')
    print('Image URL', image_url)

# Écrire les données dans un fichier CSV
with open('book_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product_page_url', 'universal_product_code_(upc)', 'title', 'price_excluding_tax',
                     'price_excluding_tax', 'Number available', 'Product description', 'Category',
                     'Review rating', 'Image URL'])
    writer.writerow([response.url, upc, title, incl_tax_price,
                     excl_tax_price, number_available, product_description,
                     category, review_rating, image_url])





