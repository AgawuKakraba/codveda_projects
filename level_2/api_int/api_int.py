import requests

api_url = "https://api.music-to-scrape.org"

# Make a GET request to fetch the raw HTML content
response = requests.get(api_url+'/charts/top-tracks')

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the desired information (e.g., songs, albums, artists) from the JSON data
    print("Top Tracks:")
    for item in data['chart']:
        print(f"Name: {item['name']}, Artist: {item['artist']}, Plays: {item['plays']}")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
                                            
                    