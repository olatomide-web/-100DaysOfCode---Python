from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("h3", class_="a-no-trucate")
song_names = [song.getText() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= '07c2858cb6c449cbb05e83771d853bab',
        client_secret= "5664b8dec2cf494d837a12bb73707d14",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["07c2858cb6c449cbb05e83771d853bab"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["https://open.spotify.com/playlist/5h6x1x4UoBNifIdQ6ooeUe?si=d57c6ba6aacd4e55&pt=77851f6e00097c08bbbc1d905201a141"], items=song_uris)
