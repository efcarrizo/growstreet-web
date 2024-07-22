import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="hoja_grow_street.png",
                 height = "100px"),
        rx.text(f"2023 - {datetime.date.today().year} Todos los derechos reservados"),
        align = 'center',
        margin = '20px'
        
        
    )