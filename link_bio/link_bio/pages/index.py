import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as const
import link_bio.utils as utlis

from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.fotter import fotter
from link_bio.styles.styles import Size as Size
from link_bio.views.lenguajes import lenguajes
from link_bio.routes import Route


@rx.page(
    route=Route.INDEX.value,
    title=utlis.index_title,
    description=utlis.index_description,
    image=utlis.preview,
    meta=utlis.index_meta # type: ignore
)

def index() -> rx.Component:
    return rx.box(
        utlis.lang(),
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=Size.BIG.value,
            padding=Size.BIG.value
            )
        ),
        fotter(),
    )