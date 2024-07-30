import reflex as rx
import growstreet_web.styles.styles as styles

def link_button(title: str, body: str, socialm: str, url: str) -> rx.Component:
    return rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon(tag = socialm,
                                width = styles.Size.BIG.value,
                                height =  styles.Size.BIG.value,
                        ),      
                    rx.vstack(
                        rx.text(title, style = styles.style_button_title),
                        rx.text(body, style = styles.style_button_subtitle),

                    
                    ),
                    ),
                    color_scheme = "teal",
                    style = styles.style_button_links,
                    
                   
                ),

           href = url,
           width = "100%",
           is_external = True,


           )
        