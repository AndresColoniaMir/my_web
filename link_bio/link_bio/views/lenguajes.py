import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, TextColor, Font
from link_bio.styles.colors import Color as Color 
from link_bio.components.title import title


def lenguajes() -> rx.Component:
    return rx.box(
        rx.image(
            src="/icons/python.svg",
            width="100%",
            height="100%",
        ),
        background_color=Color.CONTENT.value,
        border_radius=Size.DEFAULT.value,
        width="100%"
    )