import reflex as rx
from growstreet_web.components.link_button import link_button

def links() -> rx.Component:
    return rx.center(
               rx.hstack(
                    link_button("YouTube", "https://www.youtube.com/@GrowStreetCultivo"),
                    link_button("Instagram", "https://www.instagram.com/grow.street.cultivo"),
                    link_button("GitHub", "https://www.github.com/efcarrizo"),
                )
            )