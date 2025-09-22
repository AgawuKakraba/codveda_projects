from bs4 import BeautifulSoup
import requests
import csv

output_path = 'level_2/web_scraper/output.csv'
fallback_path = 'output.csv'
print("Fetching data...")

try:
    page = requests.get("https://music-to-scrape.org/")
    page.raise_for_status()
    soup = BeautifulSoup(page.text, 'html.parser')

    section = soup.find(attrs={'name': 'weekly_15'})
    data = []

    if section:
        print("Section found. Parsing songs...")
        # Find each song entry inside <p>
        items = soup.find(attrs={'name':'weekly_15'}).find_all('div', class_='center-vertical center-text')
        for item in items:
            song_tag = soup.find(attrs={'name':'weekly_15'}).find('a')
            song_text = item.get_text(strip=True)

            if song_tag and song_text:
                song_title = item.find('p').get_text(strip=True)
                artist_name = item.find('h5').get_text(strip=True)
                song_id = song_tag.get('href')
                song_link = f"https://music-to-scrape.org/{song_id}" 
                entry = [song_title, artist_name, song_link]

                # Prevent duplicates with a list check
                if entry not in data:
                    data.append(entry)
    else:
        print("No section with name='weekly_15' found.")

    print(f"✅ Scraped {len(data)} unique songs")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    data = []

finally:
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Data written to {output_path}")
        save_path = output_path
    except FileNotFoundError:
        with open(fallback_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Song", "Artist", "Artist Link"])
            writer.writerows(data)
        print(f"Directory not found. Data saved in {fallback_path} instead.")
        save_path = fallback_path

    # Optionally display contents
    u_input = input("Press y to see contents: ")
    if u_input.lower() == 'y':
        with open(save_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print("Exiting without displaying contents.")
