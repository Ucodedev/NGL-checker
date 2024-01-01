import csv
file="igfile.csv"
# Fonction pour lire les données à partir d'un fichier CSV
def read_csv(file):
    with open(file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row for row in csvreader]
    return data

# Chemin du fichier CSV
csv_file_path = 'igfile.csv'

# Charger les données depuis le fichier CSV
data = read_csv(csv_file_path)

# Extraction des noms d'utilisateur
usernames = [row[1] for row in data[1:]]

# Écriture des noms d'utilisateur dans un fichier CSV
with open('usernames.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows([[username] for username in usernames])

print("Success.")
