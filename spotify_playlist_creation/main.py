import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

time = input("What year you would like to travel to(YYYY-MM-DD): ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{time}")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary") 

song_title = [song.getText() for song in songs]




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='#',
        client_secret='#',
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = time.split("-")[0]
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{time} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)        