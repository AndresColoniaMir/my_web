
import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.styles.colors import Color as Color

def card_button(title:str,
                body:str,
                image:str,
                url:str,
                is_external=True) -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src=image,
                width="100%",
                height="82px",
            ),
            side="top",
            pb="current",
        ),
        rx.text(
            title,
            size=Spacing.SMALL.value,
            style=styles.button_title_style # type: ignore
        ),
        rx.text(
            body,
            size=Spacing.VERY_SMALL.value,
            style=styles.button_body_style # type: ignore
        ),
        on_click=rx.redirect(path=url, external=is_external),
        class_name="animate__animated animate__fadeIn"
    )