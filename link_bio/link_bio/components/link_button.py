import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def links_button(title:str, body:str, image : str, url:str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    alt=title,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style), # type: ignore
                    rx.text(body, style=styles.button_body_style), # type: ignore
                    align_items="start",
                    spacing=Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            ),
            #border_color=highlight_color,
            #border_width="2px" if highlight_color != None else None
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )
   
