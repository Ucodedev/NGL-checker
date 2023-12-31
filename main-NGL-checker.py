import csv
import requests
from bs4 import BeautifulSoup

file="usernames.csv"

# Fonction pour lire les données à partir d'un fichier CSV
def read_csv(file):
    with open(file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row[0] for row in csvreader]  # On lit la première colonne (Username)
    return data

# Fonction pour vérifier si un utilisateur existe sur la page https://ngl.link/
def check_user_exists(username):
    url = f"https://ngl.link/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    message = soup.find('p', class_='text-red-500')
    
    return "Could not find user" not in message.text if message else False

# Chemin du fichier CSV
csv_file_path = 'usernames.csv'

# Charger les usernames depuis le fichier CSV
usernames = read_csv(csv_file_path)

# Liste pour stocker les utilisateurs valides
valid_users = []

# Parcourir tous les utilisateurs
for username in usernames:
    if check_user_exists(username):
        valid_users.append(username)

# Écriture des utilisateurs valides dans un fichier CSV
with open('yes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Username"])
    csvwriter.writerows([[valid_user] for valid_user in valid_users])

print("Le fichier yes.csv a été créé avec succès pour les utilisateurs valides.")
