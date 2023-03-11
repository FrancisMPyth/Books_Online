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

# Créer un fichier CSV
with open("product_links.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Product URLs"])
    for link in product_links:
        writer.writerow([link])

# imprimer les url

    print("Product URLs:")
for link in product_links:
    print(link)