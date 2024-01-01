import csv
import requests
from bs4 import BeautifulSoup
import time

def check_username(username):
    url = f'https://ngl.link/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')

        if title_tag:
            title_text = title_tag.text.strip().lower()
            if title_text.startswith('@'):
                return True
            else:
                print(f"Title does not start with '@' for {username}. Title: {title_text}")
        else:
            print(f"No title tag found for {username}")
    elif response.status_code == 429:
        print(f"Too Many Requests (429) for {username}. Retrying after 3 seconds...")
        time.sleep(3)
        return check_username(username)
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")

    return False

def main():
    input_file = 'usernames.csv'
    output_file = 'yes.csv'

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write usernames to the output file
        for row in reader:
            username = row[0]
            if check_username(username):
                writer.writerow([username])
                # Ajouter une pause de 1 seconde entre chaque vérification
                time.sleep(1)

if __name__ == "__main__":
    main()
