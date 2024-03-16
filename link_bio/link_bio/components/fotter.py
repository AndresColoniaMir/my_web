import reflex as rx
import datetime
import link_bio.constants as constants
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color


def fotter() -> rx.Component:
    return rx.vstack(
            rx.link(
                rx.hstack(
                    rx.text(
                        f"2022-{datetime.date.today().year}",
                        font_size=Size.MEDIUM.value
                    ),
                    rx.text(
                        "Andrés Colonia.",
                        color=Color.PRIMARY.value,
                        font_size=Size.DEFAULT.value
                    ),
                ),
                href="https://github.com/AndresColoniaMir",
                is_external=True
            ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    alt="GitHub",
                    
                ),
                rx.text(
                    "HECHO CON <3 Y PACIENCIA",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                )
            ),
            href=constants.GITHUB_WEB,
            is_external=True
        ),
        align="center",
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )
  