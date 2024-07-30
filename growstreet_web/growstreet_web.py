#Importamos la libreria reflex y la llamamos rx para llamarla despues
import reflex as rx

import growstreet_web.styles.styles as styles
from growstreet_web.components.navbar import navbar
from growstreet_web.views.header.header import header
from growstreet_web.views.links.links import links
from growstreet_web.components.footer import footer
from growstreet_web.components.products_card import products_card



#Importamos el archivo styles como styles para usar sus variables
import growstreet_web.styles.styles as styles

#Los estados sirven para manejar logica python en la web
class State(rx.State):
    pass

#Por recomendacion de reflex, la funcion de la pagina principal
#se llamara index y devolvera un componente reflex
#Devuelve lo que quiero mostrar por pantalla
def index() -> rx.Component:
    return rx.box(
            navbar(),           
        # BOTON MODO OSCURO rx.color_mode.button(position="top-right", margin = '10px'),
        #Creo un stack en vertical para agrupar los siguientes elementos
            rx.vstack(
                #Componentes que estan dentro del stack
                header(),            
                #Propiedades del stack
                align = "center",
                width = "100%",             
            ),
            rx.vstack(
                products_card(),
                align = "center",
                   
            ),
            rx.vstack(
                links(),
                margin_y = styles.Size.BIG.value,
            ),
            #Hacer que el footer este en el centro
            rx.vstack(
                footer(),
            ),
          )

#Para ejecutar la app debemos definirla
app = rx.App(
    style = styles.BASE_STYLE
)
app.add_page(index)
app._compile()
