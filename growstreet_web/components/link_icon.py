import reflex as rx
import growstreet_web.styles.styles as styles

def link_icon(socialm: str, url: str) -> rx.Component:
    return rx.link(
            rx.hstack(
                rx.icon(tag = socialm,
                    width = styles.Size.BIG.value,
                    height =  styles.Size.BIG.value),      
            ),
            # color_scheme = "black",
            style = styles.style_button_links,
                
           href = url,
           width = "100%",
           is_external = True,

           )