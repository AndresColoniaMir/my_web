import reflex as rx 
import link_bio.styles.styles as styles
import link_bio.constants as const

from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.fotter import fotter
from link_bio.styles.styles import Size as Size
from link_bio.views.lenguajes import lenguajes


#class State(rx.State):
#   pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            lenguajes(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=Size.BIG.value,
            padding=Size.BIG.value
            )
        ),
        fotter(),
    )


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

app.add_page(
    index,
    image="A-Favicon-01.ico",
    title="Andrés Colonia - Desarrollador de Software",
    description="Conoce a Andrés Colonia, desarrollador de software con experiencia en Java, Python, Android y más."  
)