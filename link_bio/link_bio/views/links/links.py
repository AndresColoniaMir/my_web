import reflex as rx
from link_bio.components.link_button import links_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def links() -> rx.Component:
    return rx.vstack(
        title("Ultimos Proyectos"),
        links_button(
            "Short URL",
            "Acorta tus enlaces fácilmente.",
            "icons/link-solid.svg",
            "https://github.com/AndresColoniaMir"
            ),
        links_button(
            "Typo Gunslinger",
            "Juego tipográfico al oeste.",
            "icons/keyboard-solid.svg",
            "https://www.linkedin.com/in/andres-colonia-dev"
            ),
            links_button(
            "QuirkyWeatherWizard",
            "Clima con humor personalizado.",
            "icons/cloud-solid.svg",
            "https://github.com/AndresColoniaMir"
            ),
        links_button(
            "RPS Versus",
            "proyecto de juego de piedra, papel o tijera con mecánicas interesantes.",
            "icons/scissors-solid.svg",
            "https://www.linkedin.com/in/andres-colonia-dev"
            ),
            title("Recursos útiles"),
        links_button(
            "GitHub",
            "Repo de todos mis proyecto",
            "icons/github.svg",
            "https://github.com/AndresColoniaMir"
            ),
        links_button(
            "Linkedin",
            "Contrata me ahora",
            "icons/github.svg",
            "https://www.linkedin.com/in/andres-colonia-dev"
            ),
            links_button(
            "GitHub",
            "Repo de todos mis proyecto",
            "icons/github.svg",
            "https://github.com/AndresColoniaMir"
            ),
        links_button(
            "Linkedin2",
            "Contrata me ahora",
            "icons/github.svg",
            "https://www.linkedin.com/in/andres-colonia-dev"
            ),
        
        title("Contacto"),
        links_button(
            "Email",
            "andrescolonia24@gmail.com",
            "icons/envelope-solid.svg",
            "mailto:andrescolonia24@gmail.com"
            ),
        width="100%",
        spacing=Size.MEDIUM.value,
    )