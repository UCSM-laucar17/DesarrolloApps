import reflex as rx
from practica_reflex.practica1 import practica1_page
from practica_reflex.practica2 import practica2_page
from practica_reflex.practica3 import practica3_page
from practica_reflex.practica4 import practica4_page
from practica_reflex.ejercicio1 import ejercicio1_page
from practica_reflex.ejercicio2 import ejercicio2_page
from practica_reflex.ejercicio3 import ejercicio3_page
from practica_reflex.ejercicio4 import ejercicio4_page


@rx.page(route="/")
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Experiencias", size="8"),
        rx.hstack(
            rx.link(rx.button("Práctica 1", color_scheme="green"), href="/practica1"),
            rx.link(rx.button("Práctica 2", color_scheme="green"), href="/practica2"),
            rx.link(rx.button("Práctica 3", color_scheme="green"), href="/practica3"),
            rx.link(rx.button("Práctica 4", color_scheme="green"), href="/practica4"),
            spacing="4"
        ),
        rx.heading("Ejercicios", size="8"),
        rx.hstack(
            rx.link(rx.button("Ejercicio 1", color_scheme="purple"), href="/ejercicio1"),
            rx.link(rx.button("Ejercicio 2", color_scheme="purple"), href="/ejercicio2"),
            rx.link(rx.button("Ejercicio 3", color_scheme="purple"), href="/ejercicio3"),
            rx.link(rx.button("Ejercicio 4", color_scheme="purple"), href="/ejercicio4"),
            spacing="4"
        ),
        spacing="5",
        align="center",
        justify="center",
        min_height="100vh",
    )


app = rx.App()
app.add_page(practica1_page, route="/practica1")
app.add_page(practica2_page, route="/practica2")
app.add_page(practica3_page, route="/practica3")
app.add_page(practica4_page, route="/practica4")
app.add_page(ejercicio1_page, route="/ejercicio1")
app.add_page(ejercicio2_page, route="/ejercicio2")
app.add_page(ejercicio3_page, route="/ejercicio3")
app.add_page(ejercicio4_page, route="/ejercicio4")
