import reflex as rx
class EstadoContador(rx.State):
    conteo: int = 0

    @rx.event
    def incrementar(self):
        self.conteo += 1

    @rx.event
    def disminuir(self):
        self.conteo -= 1

    @rx.event
    def reiniciar(self):
        self.conteo = 0

def contador() -> rx.Component:
    return rx.vstack(
        rx.heading(f"Valor actual: {EstadoContador.conteo}", size="6"),
        rx.button("Incrementar", on_click=EstadoContador.incrementar),
        rx.button("Disminuir", on_click=EstadoContador.disminuir),
        rx.button("Reiniciar", on_click=EstadoContador.reiniciar),
        rx.cond(
            EstadoContador.conteo >= 0,
            rx.text("El contador es positivo", color="green"),
            rx.text("El contador es negativo", color="red"),
        ),
        spacing="3",
        align="center",
    )

def practica1_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Head", size="8"),
        rx.text("Equipo LauEriFer"),
        rx.text("Descripcion de las honey"),
        rx.button("Botón", on_click=rx.window_alert("¡Paso algo!")),
        rx.text(""),
        contador(),
        
        spacing="5",
        align="center",
        justify="center",
        padding="20px",
        background_color="#f9f9f9",
        min_height="100vh",
    )
