import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font
from link_bio.routes import Route
from link_bio.components.ant_components import float_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Andrés", as_="span", color=Color.PRIMARY.value),
                rx.text("Colonia", as_="span", color=Color.ANALOGOUS.value),
                style=styles.navbar_title_style # type: ignore
            ),
            href=Route.INDEX.value,
        ),
        float_button(
            icon=rx.image(src="/icons/mug-saucer-solid.svg", alt="Buy me a coffee"),
            href="https://www.buymeacoffee.com/andresscolonia",
        ),
        position = "sticky",
        bg= Color.CONTENT.value,
        padding_x =Size.BIG.value,
        padding_y =Size.DEFAULT.value ,
        z_index = "999",
        top="0"
    )