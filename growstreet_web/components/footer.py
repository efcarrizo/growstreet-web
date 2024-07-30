import reflex as rx
import datetime
import growstreet_web.styles.styles as styles
from growstreet_web.views.links.links_icon import links_icon

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="hoja_grow_street.png",
                 height = "100px"),
        rx.text(f"2023 - {datetime.date.today().year} Todos los derechos reservados"),
        links_icon(),
        align = "center",
        margin_top = '20px',
        padding = styles.Size.SMALL.value,
        style = styles.style_footer

        
        
    )