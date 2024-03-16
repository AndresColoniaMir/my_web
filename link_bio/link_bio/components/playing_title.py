import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.fonts import FontWeight
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import TextColor
from link_bio.styles.fonts import Font

def playing_title() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/icons/spotify.svg",
            width=styles.Size.LARGE.value,
            height=styles.Size.LARGE.value,
            alt="Icono de spotify",
            margin=Size.MEDIUM.value
        ),
        rx.text(
            "Now playing:",
            width="100%",
            font_family=Font.TITLE.value,
            font_weight=FontWeight.MEDIUM.value,
            font_size=Size.DEFAULT.value,
            color=TextColor.HEADER.value
        ),
        gap=Size.ZERO.value,
        align="center"
    )
