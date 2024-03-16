import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size

def glow_greetinng(txt:str, color:str) -> rx.Component:
    return rx.text(
        _language_start(
            txt,
            color
        ),
        font_size=Size.DEFAULT.value,
        as_="span"
    )


def _language_start(text: str, color:str) -> rx.Component:
        return rx.text(
            text,
            color=color,
            custom_attrs={
                styles.CustomAttrs.DATA_TEXT.value: text,
            },
            style=styles.glow_text_style, # type: ignore
            as_="span"
        )

