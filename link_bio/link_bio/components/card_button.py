
import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.styles.colors import Color as Color
from link_bio.components.link_icon import link_icon

def card_button(title:str,
                body:str,
                image:str,
                repo_url:str,
                url:str,
                is_external=True) -> rx.Component:
    return rx.box(
        rx.inset(
            rx.image(
                src=image,
                width="100%",
                height="100%",
                alt=title,
                border_radius=f"{Size.DEFAULT.value} {Size.DEFAULT.value} 0 0"
            ),
            side="top",
        ),
        rx.hstack(
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
            rx.spacer(),
            rx.hstack(
                link_icon(
                    "/icons/github.svg",
                    repo_url,
                    "GitHub-icon"
                ),
                link_icon(
                    "/icons/arrow-up-right.svg",
                    url,
                    "LinkedIn-icon"
                ),
                margin=Size.SMALL.value,
            ),
            margin=Size.SMALL.value,
            align="end"
        ),
        width="100%",
        style=styles.special_card
    )
