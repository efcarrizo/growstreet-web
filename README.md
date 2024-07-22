# growstreet-web

Objetivo: Crear una página web destinada a orientar a cultivadores novatos e informar sobre todos los aspectos del cultivo de c*nn*bis medicinal, proporcionando un enfoque profesional y ofreciendo amplias funciones que faciliten las tareas de los cultivadores.

Pagina web creada en python con el framework de Reflex

Version 0.1 - Prueba de Reflex
    Instalación de Reflex dejando unos ejemplos vistos en el tutorial

Version 0.2 - Components, styling
    Creación de componentes:
        *footer: Un stack vertical (rx.vstack) que contiene una imagen y texto para reutilizar en otras paginas,  align = 'center', 
                        margin = '20px' .

        *link_button: Un boton dentro de un (rx.link) que toma como parametro el texto y el url
        cada vez que lo invocamos crea un boton con esos parametros, abriendo una pestaña externa
        gracias al is_external = True.

        *navbar: Un stack que contiene una imagen del logo con el texto Grow Street

        *links: Componente que contiene 4 botones creados con el componente link button para reutilizar en distintas paginas.

        *header: Un stack con una imagen, texto y un section que contiene un texto dentro.

        Algunos componentes fueron creados dentro de carpetas para hacer las importaciones de las funciones creadas, ejemplo header que se importaba:
            from growstreet_web.views.header.header import header

        Paletas de colores creadas en "coolors", guardadas en la carpeta colorpalette

    Creación de estilos
        Todavía no se comenzo el estilado rigido, pero empezamos con el seteo de constantes que seran reutilizadas para propositos generales, como medidas y paletas de colores.