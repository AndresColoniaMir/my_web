import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color

def card_button(title:str, body:str, image:str, url:str, external:bool) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                width="100%",
                height="100%",
                alt=title,
                border_radius=f"{Size.DEFAULT.value} {Size.DEFAULT.value} 0 0"
            ),
            rx.vstack(
                rx.box(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    margin=f"{Size.SMALL.value} {Size.DEFAULT.value}"
                ),
                align_items="start",
                spacing=Size.SMALL.value,
                padding=Size.SMALL.value,
            ),
            width="100%",
            background_color=Color.CONTENT.value,
            border_radius=Size.DEFAULT.value,
            align_items="start",
            _hover={ "background_color": Color.SECONDARY.value }
        ),
        href=url,
        is_external=external,
    )