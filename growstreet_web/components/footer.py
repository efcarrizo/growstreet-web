import reflex as rx
import datetime
import growstreet_web.styles.styles as styles

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="hoja_grow_street.png",
                 height = "100px"),
        rx.text(f"2023 - {datetime.date.today().year} Todos los derechos reservados"),
        align = 'center',
        margin_top = '20px',
        # style = styles.style_footer
        style = styles.style_footer
        
        
    )