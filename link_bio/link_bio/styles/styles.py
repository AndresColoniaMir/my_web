import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font, FontWeight



# Constans
MAX_WIDTH= "560px"
FADEIN_ANIMATION = "animate__animated animate__fadeIn"
BOUNCEIN_ANIMATION = "animate__animated animate__bounceIn"

# Fonts
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Raleway:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css",
    "fonts/fonts.css",
]

class CustomAttrs(Enum):
    DATA_TEXT = "datatext"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    SUPER_BIG = "6em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"



BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.card: {
        "width": "100%",
        "height": "100%",
        "margin": Size.SMALL.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {}
    }
}


navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    color=TextColor.BODY.value
)

glow_text_style = {
    "position": "relative",
    "cursor": "pointer",
    "_after": {
        "content": f"attr({CustomAttrs.DATA_TEXT.value})",
        "position": "absolute",
        "left": "0",
        "width": "100%",
        "height": "100%",
        "opacity": "60%",
        "filter": "blur(6px)",
        "backface-visibility": "hidden",
        "-webkit-backface-visibility": "hidden",
        "-moz-backface-visibility": "hidden",
        "transform": "translateZ(0)",
        "-webkit-transform": "translateZ(0)",
        "-moz-transform": "translateZ(0)"
    },
    "_hover": {
        "_after": {
            "opacity": "100%"
        }
    }
}
project_card_style = dict(
        width="100%",
        height="100%",
        padding=Size.SMALL.value,
        border_radius=Size.DEFAULT.value,
        color=TextColor.HEADER.value,
        background_color=Color.CONTENT.value,
        white_space="normal",
        text_align="start",
        __cursor_button="pointer",
        _hover={
            "background_color": Color.SECONDARY.value
        }
)