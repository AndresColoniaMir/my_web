import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span(
                "Andrés",
                font_family=Font.TITLE.value,
                color=Color.PRIMARY.value
            ),
            rx.span(
                "Colonia",
                font_family=Font.DEFAULT.value,
                color=Color.ANALOGOUS.value
            ),
            style=styles.navbar_title_style,
        ),
        position = "sticky",
        bg= Color.CONTENT.value,
        padding_x =Size.BIG.value,
        padding_y =Size.DEFAULT.value ,
        z_index = "999",
        top="0"
    )