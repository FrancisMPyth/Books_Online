import csv
import urllib.request
from urllib.error import URLError, HTTPError

# Ouvrir le fichier CSV contenant les adresses URL
with open('product_links.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Récupérer l'adresse URL de la colonne correspondante dans la ligne actuelle
        url = row[0]
        
        # Vérifier l'adresse URL
        try:
            urllib.request.urlopen(url)
            print(f"{url} est une adresse URL valide.")
        except HTTPError as e:
            print(f"Erreur HTTP lors de la vérification de {url} : {e.code} {e.reason}")
        except URLError as e:
            print(f"Erreur de connexion lors de la vérification de {url} : {e.reason}")
        except:
            print(f"Erreur inattendue lors de la vérification de {url}")
