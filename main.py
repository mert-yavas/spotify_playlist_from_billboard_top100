import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# SPOTIFY ACCOUNT INFORMATION
CLIENT_ID = "YOUR SPOTIFY CLIENT ID"
CLIENT_SECRET = "YOUR SPOTIFY CLIENT SECRET"

# Input the desired date for Billboard 100 chart
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

# Scraping Billboard 100 chart for the specified date
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")
song_elements = soup.find_all(class_="o-chart-results-list-row-container")
song_names = []

# Extracting song names from the Billboard 100 chart
for song_element in song_elements:
    song = song_element.find(name="h3").getText().strip()
    song_names.append(song)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:3000",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Obtaining user ID from the authenticated Spotify account
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title and adding them to the playlist
song_uris = []
year = date.split("-")[0]
for song_name in song_names:
    result = sp.search(q=f"track:{song_name} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
