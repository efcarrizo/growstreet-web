import reflex as rx
import growstreet_web.styles.styles as styles

def products_card() -> rx.Component:
    return rx.hstack(
                rx.flex(
                    rx.card(
                        rx.link(
                            rx.flex(
                                rx.image(src="/products/top_deeper_250_embase.png",
                                            height = "120px"),
                                rx.box(
                                    rx.heading("Top DEEPER"),
                                    rx.text("Top Candy es un potenciador de floración formulado para aumentar el contenido de"),
                                    rx.text("azúcares y resinas en las flores de cannabis. Mejora el sabor y el aroma final del producto,"),
                                    rx.text("proporcionando cogollos más densos y resinosos"),
                                ),
                                spacing="2",
                                direction = "column",
                                align = "center"
                                
                            ),
                            # href="PAGINA DEL PRODUCTO"
                        ),
                        as_child=True,
                        #Tamaño total de la card
                        width = "300px"

                    ),

                    rx.card(
                        #La idea de este link es que dirija directo a la venta
                        rx.link(
                            #Dentro de este link pruebo con vstack
                            rx.vstack(    
                                rx.image(src="/products/top_veg_250_embase.png",
                                            height = "120px"),
                                    rx.box(
                                        rx.heading("Top VEG"),
                                        rx.text("Top Candy es un potenciador de floración formulado para aumentar el contenido de"),
                                        rx.text("azúcares y resinas en las flores de cannabis. Mejora el sabor y el aroma final del producto,"),
                                        rx.text("proporcionando cogollos más densos y resinosos"),
                                    ),
                                    spacing="2",
                                    align = "center"
                            ),
                            # href="PAGINA DEL PRODUCTO"
                        ),
                            as_child=True,
                            #Tamaño total de la card
                            width = "300px",

                        ),

                        rx.card(
                                rx.link(
                                    rx.flex(
                                        rx.image(src="/products/top_bloom_250_embase.png",
                                                 height = "120px"),
                                        rx.box(
                                            rx.heading("Top BLOOM"),
                                            rx.text("Top Candy es un potenciador de floración formulado para aumentar el contenido de"),
                                            rx.text("azúcares y resinas en las flores de cannabis. Mejora el sabor y el aroma final del producto,"),
                                            rx.text("proporcionando cogollos más densos y resinosos"),
                                        ),
                                        spacing="2",
                                        direction = "column",
                                        align = "center"
                                    ),
                                    # href="PAGINA DEL PRODUCTO"
                                ),
                                as_child=True,
                                #Tamaño total de la card
                                width = "300px"

                            ),

                            rx.card(
                                rx.link(
                                    rx.flex(
                                        rx.image(src="/products/top_candy_250_embase.png",
                                                 height = "120px"),
                                        rx.box(
                                            rx.heading("Top CANDY"),
                                            rx.text("Top Candy es un potenciador de floración formulado para aumentar el contenido de"),
                                            rx.text("azúcares y resinas en las flores de cannabis. Mejora el sabor y el aroma final del producto,"),
                                            rx.text("proporcionando cogollos más densos y resinosos"),
                                            
                                        ),
                                        spacing="2",
                                        direction = "column",
                                        align = "center"
                                    ),
                                    # href="PAGINA DEL PRODUCTO"
                                ),
                                as_child=True,
                                #Tamaño total de la card
                                width = "300px"

                            ),

                    #Propiedades dentro del flex
                    spacing = styles.Size.BIG.value,
                    justify = "center",
                    width = "100%",
                    wrap = "wrap"
                    
                ),
                
                #Props de hstack
                width = "100%",
                margin_y = styles.Size.BIG.value,

    )