import reflex as rx
import link_bio.styles.styles as styles

from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color



def info_languages(image: str) -> rx.Component:
    return rx.image(
            src=image,
            width=styles.Size.LARGE.value,
            height=styles.Size.LARGE.value,
            )
    