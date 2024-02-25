import reflex as rx
import link_bio.constants as constants
from link_bio.components.link_icon import link_icon
from link_bio.components.info_languages import info_languages
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Andrés Colonia",
                size="xl",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Andrés Colonia",
                    size="lg",
                    color = TextColor.HEADER.value
                ),
                rx.hstack(
                link_icon("icons/github.svg",constants.GITHUB_URL, "GitHub-icon"),
                link_icon("icons/linkedin.svg",constants.LINKEDIN_URL, "LinkedIn-icon"),
                width="100%",
                spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value,
        ),       
        rx.text(
            """¡Bienvenidos a mi mundo digital! Soy Andrés Colonia, 
            desarrollador de software con un enfoque backend, hábil
            en Java, Python, C#, HTML, CSS y SQL,
            mi compromiso es llevar tu proyecto al siguiente
            nivel.""",
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value
        ),
        width="100%",
        spacing=Size.BIG.value,  
        align_items="start"
    )
    
    
    