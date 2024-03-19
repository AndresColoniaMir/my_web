import reflex as rx
import link_bio.styles.styles as stiles
from link_bio.styles.styles import Size as Size


def link_icon(image:str, url: str, alt:str, side="top") -> rx.Component:
    return rx.link(
            rx.tooltip(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    alt=alt,
                ),
                content=f"Visita mi perfil en {alt}",
                side=side  
            ),
        href=url,
        is_external=True
    ) 
        
        
    