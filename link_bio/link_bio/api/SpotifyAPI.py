
import dotenv
import os
import requests
import time
from link_bio.model.Track import Track 

class SpotifyAPI:

    dotenv.load_dotenv()

    CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

    def __init__(self) -> None:
        self.token = None
        self.token_expires = 0

    def regenerate_token(self):
        token_url = "https://accounts.spotify.com/api/token"
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': self.REFRESH_TOKEN,
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(token_url, data=payload, headers=headers)
        if response.status_code == 200:
            self.token = response.json()['access_token']
            self.token_expires = time.time() + response.json()['expires_in']
        else:
            self.token = None
            self.token_expires = 0

    def token_valid(self) -> bool:
        return time.time() < self.token_expires
    
    def live_playing(self) -> Track:
        
        if not self.token_valid():
            self.regenerate_token()

        url = "https://api.spotify.com/v1/me/player/currently-playing"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            track_info = {
                "name": data["item"]["name"],
                "artists": [artist["name"] for artist in data["item"]["artists"]],
                "album_image": next((image["url"] for image in data["item"]["album"]["images"] if image["height"] == 300), None),
                "is_playing": data["is_playing"],
                "duration_ms": data["item"]["duration_ms"],
                "progress_ms": data["progress_ms"],
                "href": data["item"]["external_urls"]["spotify"],
                "live": True
            }
        
            return Track(
                image=track_info["album_image"],
                name=track_info["name"],
                artists=f", ".join(track_info["artists"]),
                href=track_info["href"],
                duration=track_info["duration_ms"],
                progress=track_info["progress_ms"],
                live=track_info["live"],
                is_playing=track_info["is_playing"]
            )
        else:   
            return Track(
                image="",
                name="",
                artists="",
                href="",
                duration=0,
                progress=0,
                live=False,
                is_playing=False
            )