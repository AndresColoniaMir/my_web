import reflex as rx

from link_bio.components.info_languages import info_languages
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color


def lenguajes() -> rx.Component:
    return  rx.hstack(
        info_languages("icons/java.svg", "Java"),
        rx.spacer(),
        info_languages("icons/python.svg", "Python"),
        rx.spacer(),
        info_languages("icons/html5.svg" , "HTML5"),
        rx.spacer(),
        info_languages("icons/css3-alt.svg" , "CSS3"),
        rx.spacer(),
        info_languages("icons/android.svg" , "Android"),
        width="100%",
    ),