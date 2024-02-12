import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def fotter() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"2022-{datetime.date.today().year} Andrés Colonia.",
                href="https://github.com/AndresColoniaMir",
                is_external=True,
                font_size=Size.MEDIUM.value
            ),
        rx.text(
            "Heco con <3",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
            ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value
    )