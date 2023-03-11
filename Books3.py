import requests
import csv
from bs4 import BeautifulSoup

# URL de la page de la catégorie 
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# Obtenir le contenu HTML de la page
response = requests.get(url)
html = response.content

# Parser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Trouver tous les liens des pages Produit
product_links = []
for product in soup.find_all("h3"):
    link = product.find("a")["href"]
    product_links.append("http://books.toscrape.com/catalogue/" + link)
for link in product_links:
    print(link)

# Stocker les informations de chaque produit dans une liste de dictionnaires
products_data = []

for link in product_links:
    # Obtenir le contenu HTML de la page de produit
    response = requests.get(link)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

   # Envoie de la requête HTTP
    response = requests.get(url)
   # Vérification du code d'état HTTP 
if response.status_code == 200:
    # Extraction du contenu HTML
    html = response.content
    # Initialisation de BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # verification  des informations demandées
    
    # Stocker les informations de chaque produit dans une liste de dictionnaires
products_data = []

for link in product_links:
    # Obtenir le contenu HTML de la page de produit
    response = requests.get(link)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    # product_page_url
    print('product_page_url' , response.url)
    # UPC
    upc = soup.find("td").text
    # Afficher UPC
    print('universal_product_code_(upc)' , upc)