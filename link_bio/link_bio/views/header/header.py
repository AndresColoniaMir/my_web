import reflex as rx
import link_bio.constants as constants

from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def header(details = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="Andrés Colonia",
                    size="xl",
                    #src="/images/andres.jpg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}" 
                ),
            position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Andrés Colonia",
                    size=Spacing.BIG.value # type: ignore
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        constants.GITHUB_URL,
                        "GitHub-icon"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        constants.LINKEDIN_URL,
                        "LinkedIn-icon"
                    ),
                    spacing=Size.LARGE.value,
                    padding_top=Size.SMALL.value
                ),  
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Size.BIG.value,
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.text(
                    """Soy Andrés Colonia, desarrollador de software,
                    hábil en Java, Python, C#, HTML, CSS y SQL,
                    mi compromiso es llevar tu proyecto al siguiente
                    nivel.""",
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Size.BIG.value
            )
        ),
        width="100%",
        spacing=Size.BIG.value,
        align_items="start"
    )
    