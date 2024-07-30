# growstreet-web

Objetivo: Crear una página web destinada a orientar a cultivadores novatos e informar sobre todos los aspectos del cultivo de c*nn*bis medicinal, proporcionando un enfoque profesional y ofreciendo amplias funciones que faciliten las tareas de los cultivadores.

Pagina web creada en python con el framework de Reflex

Version 0.1 - Prueba de Reflex
    Instalación de Reflex dejando unos ejemplos vistos en el tutorial

Version 0.2 - Components, styling
    Creación de componentes:
        footer: Un stack vertical (rx.vstack) que contiene una imagen y texto para reutilizar en otras paginas,  align = 'center', 
                        margin = '20px' .

        link_button: Un boton dentro de un (rx.link) que toma como parametro el texto y el url
        cada vez que lo invocamos crea un boton con esos parametros, abriendo una pestaña externa
        gracias al is_external = True.

        navbar: Un stack que contiene una imagen del logo con el texto Grow Street

        links: Componente que contiene 4 botones creados con el componente link button para reutilizar en distintas paginas.

        header: Un stack con una imagen, texto y un section que contiene un texto dentro.

        Algunos componentes fueron creados dentro de carpetas para hacer las importaciones de las funciones creadas, ejemplo header que se importaba:
            from growstreet_web.views.header.header import header

        Paletas de colores creadas en "coolors", guardadas en la carpeta colorpalette

    Creación de estilos
        Todavía no se comenzo el estilado rigido, pero empezamos con el seteo de constantes que seran reutilizadas para propositos generales, como medidas y paletas de colores.

Version 0.3 Styling

    navbar: Se hizo una modificacion en la foto y el texto de la barra de navegación, se presento la posible estructura.
    
    title: Se creo un componente para los titulos y se estilo en el
    archivo style.py, para no utilizar las propiedades del heading
    se estilo mediante props de CSS

    links: Se agregaron iconos y se dejaron presentados los links, todavia hay que realizar modificaciones y posicionarlos.

    header: Se le agrego el title ahi para realizar pruebas.

Version 0.4 Styling

    link_icon: Se creo un nuevo componente que pide como parametro el nombre del icono y la direccion, se utiliza en links_icon
    Estan dentro del footer(todavia faltan modificaciones).

    products_card : Se modificaron los tamaños de las cards(todavia faltan modificaciones).

    Se modifico dentro del header el padding del section para que no queden las letras en los limites.

    

    

    