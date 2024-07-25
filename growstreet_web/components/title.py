from turtle import width
import reflex as rx
import growstreet_web.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
            text,
            #Para no utilizar las props de heading
            # se trae todo del style pero con nombres distintos
            # para poder modificar 
            # align = "center",
            # size = "3",
            style = styles.style_title

            )