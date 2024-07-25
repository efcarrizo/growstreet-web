import reflex as rx
from enum import Enum
from growstreet_web.views.header.header import header

#Defino una constante para poder usarla cuando quieras.

#Contants
MAX_WIDTH = "600px"

#Creamos la clase para definir las constantes
class Size(Enum):
    #Sizes
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"

class Colors(Enum):
    #Pallet Colors
    AZUL = "#0B7099"
    VERDEAZULADO = "#57BF98"
    VERDEOSCURO = "#15856C"
    NARANJA = "#F06449"
    NEGRO = "#0D0A0B"

# Creamos un style general para todos los botones
BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

#Estilos para botones especificos
style_button_links = dict(
    # Alinear el contenido al inicio
    justifyContent = "start",
)

#Configuracion para titulos
style_title = dict(
    #Toma todo el bloque de linea
    width = "100%",
    #Para no usar align en el componente
    textAlign = "center",
    #Para no usar size en el componente retocamos la fuente
    font_size = Size.DEFAULT,
    #Color del texto
    color = Colors.NARANJA
)


#Para crear un estilo especifico para un componente
style_button_title = dict(
    font_size = Size.MEDIUM.value,
)
style_button_subtitle = dict(
    font_size = Size.SMALL.value,
)

style_footer = dict(
    bg = Colors.NARANJA.value,
    width = "100%",
)
