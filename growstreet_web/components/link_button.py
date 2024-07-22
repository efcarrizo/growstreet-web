import reflex as rx
import growstreet_web.styles.styles as styles

def link_button(texto: str, url: str) -> rx.Component:
    return rx.link(
            rx.button(texto, color_scheme = "teal"),
            href = url,
            is_external = True
            )
        