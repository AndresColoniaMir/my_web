import reflex as rx
import link_bio.constants as constants

from link_bio.components.link_button import links_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.routes import Route
from link_bio.styles.colors import Color as Color

def links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        links_button(
            "Proyectos",
            "Echa un vistazo a todos mis proyectos",
            "icons/terminal-solid.svg",
            Route.PROJECTS.value,
            is_external=False,
            highlight_color=Color.PRIMARY.value
        ),
        title("Ultimos Proyectos"),
        links_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "icons/link-solid.svg",
            constants.SHORT_URL
        ),
        links_button(
            "Typo Gunslinger",
            "Desafíos tipográficos con un toque del salvaje oeste.",
            "icons/keyboard-solid.svg",
            constants.TYPO_GUNSLINGER
        ),
            links_button(
            "QuirkyWeatherWizard",
            "Clima y humor personalizado.",
            "icons/cloud-solid.svg",
            constants.QUIRKY_WEATHER_WIZARD
        ),
        links_button(
            "RPS Versus",
            "Juego de cartas estratégico basado en el clásico piedra, papel o tijera.",
            "icons/scissors-solid.svg",
            constants.RPS_VERSUS
        ),
        title("Contacto y CV"),
        links_button(
            "Email",
            "andrescolonia24@gmail.com",
            "icons/envelope-solid.svg",
            f"mailto:{constants.EMAIL}"
        ),
        links_button(
            "CV",
            "Ver y descarga mi CV",
            "icons/file-arrow-down-solid.svg",
            "/pdfs/AndresColonia-CV-2024-v6.pdf"
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )