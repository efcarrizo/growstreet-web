import reflex as rx
import growstreet_web.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src = "hoja_grow_street.png",
            height = "25px"
        ),
        rx.text(
            "Grow Street",
            color = "white",
            height = "25px",
                 
        ),
        position = "sticky",
        bg=styles.Constant.AZUL,
        padding_x = "5px",
        padding_y = "8px",
        z_index = "999"
    )