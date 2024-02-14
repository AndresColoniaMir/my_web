import reflex as rx
import link_bio.constants as constants
from link_bio.components.link_button import links_button
from link_bio.components.download_button import download_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def links() -> rx.Component:
    return rx.vstack(
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
            "Juego de cartas estratégico basado en el clasico piedra, papel o tijera.",
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
        download_button(
            "CV",
            "Descarga mi CV",
            "icons/file-solid.svg",
            "/pdfs/Andres Colonia-CV-2023-v3.pdf"
            ),
        width="100%",
        spacing=Size.MEDIUM.value,
    )