from re import M
import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
            rx.image(src="grow_street_logo.png",
                    height = "300px"),
            rx.text("Bienvenidos a Grow Street"),
            rx.text("""Nuestro contenido es explicativo 
                    para guiar a personas que quieran iniciar 
                    en el mundo del cultivo"""),
            rx.text("Cultivo actual Mother Gorilla / Royal Queen Seeds"),
            rx.section( 
            rx.heading("Mother Gorilla"),
            rx.text("""Actualmente nos encontramos cultivando mother gorilla
                    del banco Royal Queen"""),
                padding_left="12px",
                padding_right="12px",
                background_color="var(--pink-2)",
                ),
                align = "center",
            )