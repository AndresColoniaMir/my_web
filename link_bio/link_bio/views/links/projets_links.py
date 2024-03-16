import reflex as rx
import link_bio.constants as constants

from link_bio.components.card_button import card_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.routes import Route
from link_bio.styles.colors import Color as Color

def projets_links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        card_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "/icons/terminal-solid.svg",
            constants.SHORT_URL
        ),
        card_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "/icons/terminal-solid.svg",
            constants.SHORT_URL
        ),
        card_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "/icons/terminal-solid.svg",
            constants.SHORT_URL
        ),
        card_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "/icons/terminal-solid.svg",
            constants.SHORT_URL
        ),
        card_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "/icons/terminal-solid.svg",
            constants.SHORT_URL
        ),
        card_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "/icons/terminal-solid.svg",
            constants.SHORT_URL
        ),
        card_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "/icons/terminal-solid.svg",
            constants.SHORT_URL
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )   