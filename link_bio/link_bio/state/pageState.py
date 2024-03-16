import reflex as rx
import pytz
import link_bio.utils as utils

from datetime import datetime
from link_bio.api.api import live_playing
from link_bio.model.Track import Track 
from link_bio.styles.colors import Color, TextColor

class PageState(rx.State):

    timezone = ""
    now: datetime = datetime.now()
    greeting = ""
    greeting_color = ""

    track_status = Track(
        image="",
        name="",
        artists="",
        href="",
        duration=0,
        progress=0,
        live=False,
        is_playing=False
    )

    async def chec_track(self):
        self.track_status = await live_playing()


    def check_timezone(self):
        if self.timezone == "":
            return rx.call_script(
                utils.LOCAL_TIMEZONE_SCRIPT,
                PageState.update_timezone
            )
        else:
            self.update_timezone(self.timezone)

    def update_timezone(self, timezone: str):
        self.timezone = timezone
        self.now = datetime.now(pytz.timezone(timezone))
    
    def update_greeting(self):
        if self.now.hour < 12:
            self.greeting = "¡Buenos días! 🌞."
            self.greeting_color = TextColor.YELLOW.value
        elif self.now.hour < 18:
            self.greeting = "¡Hey! ¡Buenas tardes! 😊."
            self.greeting_color = Color.PRIMARY.value
        else:
            self.greeting = "¡Hola! ¡Buenas noches! 🌙."
            self.greeting_color = TextColor.PURPLE.value
