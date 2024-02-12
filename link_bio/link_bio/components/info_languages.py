import reflex as rx
import link_bio.styles.styles as styles

from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color



def info_languages(image: str, title:str) -> rx.Component:
    return rx.hstack(
        rx.image(
            src=image,
            width=styles.Size.LARGE.value,
            height=styles.Size.LARGE.value,
            color=Color.PRIMARY.value
        ),
        rx.text(
            f" {title} ",
            font_size=Size.MEDIUM.value,
            color = TextColor.BODY.value
        )
         
    )