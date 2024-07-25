from ctypes import alignment
from turtle import width
import reflex as rx
import growstreet_web.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
                rx.hstack(
                    rx.box(
                    rx.image(
                        src = "hoja_grow_street.png",
                        height = styles.Size.BIG.value
                    ),

                        background_color="white",
                        border_radius = "20px",
                        margin="4px",
                        padding="4px",
                    ),
                    rx.text.strong(
                        "Grow Street",
                        color = "white",
                                               
                    ),
                    align_items = "center",
                    width = "50%"           
                ),
                rx.hstack(
                    rx.text(
                        "Tienda",
                        color = "white",
                    ),
                    rx.text(
                        "Guia de cultivo",
                        color = "white",
                    ),
                    rx.text(
                        "Sobre nosotros",
                        color = "white",
                    ),
                    width = "50%",
                    justify = "end",
                    
                ),
            align_items = "center",
            position = "sticky",
            bg=styles.Colors.AZUL,
            padding_x = styles.Size.DEFAULT.value,
            padding_y = styles.Size.SMALL.value,
            z_index = "999",
            top = "0"
           )