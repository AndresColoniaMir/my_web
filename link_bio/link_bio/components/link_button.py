import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size, Spacing

def links_button(title:str,
                body:str,
                image:str,
                url:str, 
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:
    return rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    alt=title,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
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
                    align_items="start",
                    spacing=Spacing.ZERO.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                align="center",
                width="100%"
            ),
            border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
            class_name=styles.BOUNCEIN_ANIMATION if animated else None,
            on_click=rx.redirect(path=url, external=is_external)
        )
