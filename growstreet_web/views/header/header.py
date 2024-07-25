import reflex as rx
import growstreet_web.styles.styles as styles
from growstreet_web.components.title import title

def header() -> rx.Component:
    return rx.vstack(
            rx.image(src="grow_street_logo.png",
                height = "350px"),
            title("Bienvenidos a Grow Street"),
            rx.text("""Nuestro contenido es explicativo 
                    para guiar a personas que quieran iniciar 
                    en el mundo del cultivo"""),
            rx.text("Cultivo actual Mother Gorilla / Royal Queen Seeds"),
            rx.section( 
            rx.heading("Mother Gorilla"),
            rx.text("""Actualmente nos encontramos cultivando mother gorilla
                    del banco Royal Queen"""),
                background_color="var(--pink-2)",
            ),
            margin_x = styles.Size.DEFAULT.value,
            align = "center",
            )