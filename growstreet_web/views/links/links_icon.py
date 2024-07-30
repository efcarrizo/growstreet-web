import reflex as rx
from growstreet_web.components.link_icon import link_icon

def links_icon() -> rx.Component:
    return rx.hstack(
                link_icon("instagram","https://instagram.com/grow.street.cultivo"),
                link_icon("youtube","https://www.youtube.com/@GrowStreetCultivo"),
            )