import reflex as rx
import link_bio.constants as constants

from link_bio.components.glow_greetinng import glow_greetinng
from link_bio.components.link_icon import link_icon
from link_bio.components.current_track import current_track
from link_bio.components.playing_title import playing_title
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.state.pageState import PageState


def header(details = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(                  
                    name="Andrés Colonia",
                    size=Spacing.MEDIUM_BIG.value,
                    #src="/images/andres.jpg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}" 
                ),
            position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Andrés Colonia",
                    size=Spacing.BIG.value # type: ignore
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        constants.GITHUB_URL,
                        "GitHub-icon"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        constants.LINKEDIN_URL,
                        "LinkedIn-icon"
                    ),
                    spacing=Spacing.DEFAULT.value,
                    padding_top=Size.SMALL.value
                ),  
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="center",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            PageState.track_status.live,
            rx.vstack(
                playing_title(),    
                current_track(
                    PageState.track_status.image,
                    PageState.track_status.name,
                    PageState.track_status.artists,
                    PageState.track_status.href,
                    highlight_color=Color.GREEN_SPOTIFY.value,
                    animated=True
                ),
                spacing=Spacing.ZERO.value,
                width="100%",
                align_items="start"
            ),   
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.text(
                    glow_greetinng(f"{PageState.greeting}", PageState.greeting_color), 
                    """ Soy Andrés Colonia, desarrollador de software,
                    hábil en Java, Python, C#, HTML, CSS y SQL, mi compromiso es 
                    llevar tu proyecto al siguiente
                    nivel.""",
                    font_size=Size.DEFAULT.value,   
                    color=TextColor.BODY.value,
                    as_="span"
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
        on_mount=[PageState.chec_track, PageState.check_timezone, PageState.update_greeting]
    )
    