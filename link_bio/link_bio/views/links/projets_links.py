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
            "Este sitio web",
            "Web personal con enlaces a mis proyectos y CV.",
            "/my_web.png",
            constants.GITHUB_WEB,
            "#"
        ),
        card_button(
            "Short URL (W.I.P)",
            "Acorta tus enlaces fácilmente.",
            "/icons/link-solid.svg",
            constants.SHORT_URL,
            "#"
        ),
        card_button(
            "Typo Gunslinger (W.I.P)",
            "Desafíos tipográficos con un toque del salvaje oeste.",
            "/icons/keyboard-solid.svg",
            constants.TYPO_GUNSLINGER,
            "#"
        ),
        card_button(
            "QuirkyWeatherWizard (W.I.P)",
            "Clima y humor personalizado.",
            "/icons/cloud-solid.svg",
            constants.QUIRKY_WEATHER_WIZARD,
            "#"
        ),
        card_button(
            "RPS Versus (W.I.P)",
            "Juego de cartas estratégico basado en el clásico piedra, papel o tijera.",
            "/icons/scissors-solid.svg",
            constants.RPS_VERSUS,
            "#"
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )   