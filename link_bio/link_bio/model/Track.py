import reflex as rx

class Track(rx.Base):
    image: str
    name: str
    artists: str
    href: str
    duration: int
    progress: int
    live: bool
    is_playing: bool
