import reflex as rx
import link_bio.constants as constants

from link_bio.components.project_card import project_card
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.routes import Route
from link_bio.styles.colors import Color as Color

def projets_links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        project_card(
            "Este sitio web",
            "Web de links y proyectos hecha con Python puro y Reflex.",
            "/images/my_web.png",
            constants.GITHUB_WEB,
            "#"
        ),
        project_card(
            "Short URL (W.I.P)",
            "Acorta tus enlaces fácilmente.",
            "/images/Short_URL.jpg",
            constants.SHORT_URL,
            "#"
        ),
        project_card(
            "Typo Gunslinger (W.I.P)",
            "Desafíos tipográficos con un toque del salvaje oeste.",
            "/images/Typo_Gunslinger.jpg",
            constants.TYPO_GUNSLINGER,
            "#"
        ),
        project_card(
            "QuirkyWeatherWizard (W.I.P)",
            "Clima y humor personalizado.",
            "/images/QuirkyWeatherWizard.jpg",
            constants.QUIRKY_WEATHER_WIZARD,
            "#"
        ),
        project_card(
            "RPS Versus (W.I.P)",
            "Juego de cartas estratégico basado en el clásico piedra, papel o tijera.",
            "/images/RPS_Versus.jpg",
            constants.RPS_VERSUS,
            "#"
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )   