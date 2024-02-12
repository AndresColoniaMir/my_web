import reflex as rx
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
                link_icon("icons/github.svg","https://github.com/AndresColoniaMir"),
                link_icon("icons/linkedin.svg","https://github.com/AndresColoniaMir"),
                #link_icon("icons/x-twitter.svg","https://github.com/AndresColoniaMir"),
                #link_icon("icons/instagram.svg","https://github.com/AndresColoniaMir"),
                spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value,
        ),
        rx.hstack(
                info_languages("icons/java.svg","Java"),
                rx.spacer(),
                info_languages("icons/python.svg","Python"),
                rx.spacer(),
                info_languages("icons/html5.svg","HTML"),
                rx.spacer(),
                info_languages("icons/css3-alt.svg","CSS"),
                rx.spacer(),
                info_languages("icons/android.svg","Android"),
                width="100%"
        ),
        rx.text(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                 sed do eiusmod tempor incididunt ut labore et dolore magna
                 aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                 ullamco laboris nisi ut aliquip ex ea commodo consequat.
                 """,
                 font_size=Size.DEFAULT.value,
                 color=TextColor.BODY.value
        ),
        width="100%",
        spacing=Size.BIG.value,  
    )
    
    
    