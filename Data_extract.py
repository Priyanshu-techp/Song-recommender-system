import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# ====== Spotify Credentials ======
CLIENT_ID = "d6f1adb859ee44d79ea8992ab2ee62c6"
CLIENT_SECRET = "01781d8e6539440c9d643cf447cca3c0"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

SCOPE = "user-library-read"

# ====== Auth Setup ======
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# ====== Fetch User Library ======
all_songs = []
results = sp.current_user_saved_tracks(limit=50)
while results:
    for item in results['items']:
        track = item['track']

        # Track info
        track_id = track['id']
        track_name = track['name']
        spotify_url = track['external_urls']['spotify']

        # Album info
        album_name = track['album']['name']
        album_type = track['album']['album_type']
        label = track['album'].get('label', None)
        album_image_url = track['album']['images'][0]['url'] if track['album']['images'] else None

        # Artist info (first artist for details)
        artist_id = track['artists'][0]['id']
        artist_data = sp.artist(artist_id)
        artist_name = artist_data['name']
        genres = ", ".join(artist_data['genres']) if artist_data['genres'] else None

        song_info = {
            "Track ID": track_id,
            "Track Name": track_name,
            "Artist(s)": ", ".join([artist['name'] for artist in track['artists']]),
            "Spotify URL": spotify_url,
            "Artist Name": artist_name,
            "Genres": genres,
            "Album Name": album_name,
            "Album Type": album_type,
            "Label": label,
            "Album Image URL": album_image_url   # ✅ Added image URL
        }

        all_songs.append(song_info)

    # pagination (next batch of songs)s\
    if results['next']:
        results = sp.next(results)
    else:
        results = None

# ====== Save to CSV ======
df = pd.DataFrame(all_songs)
df.to_csv("spotify_library.csv", index=False)

print("✅ Your Spotify library with images has been saved to spotify_library.csv")
