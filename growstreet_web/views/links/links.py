import reflex as rx
from growstreet_web.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
                rx.text(
                    """Seguinos en nuestras redes""",
                    align = "center"
                ),
                rx.hstack(
                link_button(
                    "YouTube",
                    "Contenido acerca de nuestros cultivos",
                    "youtube",
                    "https://www.youtube.com/@GrowStreetCultivo"
                ),

                link_button("Instagram",
                            "Seguinos en instagram para ver las novedades",
                            "instagram",                         
                            "https://www.instagram.com/grow.street.cultivo"
                ),
                
                link_button("GitHub",
                            "Mis otros proyectos web",
                            "github",
                            "https://www.github.com/efcarrizo"
                ),
                #El bloque que contiene los botones de links
                width = "100%",          
                ),

                #Bloque que esta por fuera de los links
                width = "100%",
                align = "center",
                padding_x = "10%",
              
            ),

