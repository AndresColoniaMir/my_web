from .SpotifyAPI import SpotifyAPI
from link_bio.model.Track import Track 


SPOTIFY_API = SpotifyAPI() 


async def live_playing() -> Track:
    return SPOTIFY_API.live_playing()

def hello() -> str:
    return "!Hey Hola! 👋"