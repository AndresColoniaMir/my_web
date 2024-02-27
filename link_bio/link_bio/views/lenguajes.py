import reflex as rx

from link_bio.components.info_languages import info_languages



def lenguajes() -> rx.Component:
    return  rx.hstack(
        info_languages("/icons/python.svg", "Python"),
        max_width="100%",
    )