import reflex as rx 
import link_bio.styles.styles as styles
import link_bio.constants as const
from link_bio.pages.index import index
from link_bio.pages.projets import projects

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE, # type: ignore
     head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)

