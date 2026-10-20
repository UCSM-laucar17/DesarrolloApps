import reflex as rx
import re

class EstadoContacto(rx.State):
    mensaje_respuesta: str = ""
    color_respuesta: str = "black"

    @rx.event
    def enviar(self, datos: dict[str, str]):
        nombre = datos.get("nombre", "").strip()
        correo = datos.get("correo", "").strip()
        mensaje = datos.get("mensaje", "").strip()

        if not nombre:
            self.mensaje_respuesta = "Error: El nombre no debe estar vacío."
            self.color_respuesta = "red"
            return

        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron_correo, correo):
            self.mensaje_respuesta = "Error: El correo no es válido."
            self.color_respuesta = "red"
            return

        if not mensaje:
            self.mensaje_respuesta = "Error: El mensaje no debe estar vacío."
            self.color_respuesta = "red"
            return
        
        if len(mensaje) < 10:
            self.mensaje_respuesta = "Error: Mínimo 10 caracteres."
            self.color_respuesta = "red"
            return

        self.mensaje_respuesta = f"¡Gracias {nombre}! Enviado correctamente."
        self.color_respuesta = "green"

        return [
            rx.set_value("nombre_input", ""),
            rx.set_value("correo_input", ""),
            rx.set_value("mensaje_input", "")
        ]


def formulario_contacto() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    name="nombre",
                    id="nombre_input",
                    placeholder="Nombre completo",
                    required=True
                ),
                rx.input(
                    name="correo",
                    id="correo_input",
                    type="email",
                    placeholder="Correo electrónico",
                    required=True
                ),
                rx.text_area(
                    name="mensaje",
                    id="mensaje_input",
                    placeholder="Mensaje (mínimo 10 car.)",
                    required=True
                ),
                rx.button("Enviar", type="submit", width="100%"),
                spacing="3",
                width="100%"
            ),
            on_submit=EstadoContacto.enviar,
            width="100%",
            max_width="400px"
        ),
        rx.cond(
            EstadoContacto.mensaje_respuesta != "",
            rx.text(EstadoContacto.mensaje_respuesta, color=EstadoContacto.color_respuesta),
        ),
        spacing="4",
        align="center",
        width="100%"
    )


def practica3_page() -> rx.Component:
    return rx.vstack(
        formulario_contacto(),
        rx.link(rx.button("Volver", variant="outline"), href="/"),
        spacing="5",
        align="center",
        justify="center",
        padding="40px",
        min_height="100vh",
    )
