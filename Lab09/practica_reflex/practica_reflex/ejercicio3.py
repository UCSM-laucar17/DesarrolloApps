import reflex as rx
import re

class Ejercicio3State(rx.State):
    solicitudes: list[dict[str, str]] = []
    mensaje: str = ""
    error: str = ""
    #formulario
    def procesar_formulario(self, datos: dict):
        self.mensaje = ""
        self.error = ""
        #Constructor de variable a diccionario
        nombre = datos.get("nombre", "").strip()
        correo = datos.get("correo", "").strip()
        tipo = datos.get("tipo", "").strip()
        descripcion = datos.get("descripcion", "").strip()
        #Confirmar todos los campos obligatorios
        if not nombre or not correo or not tipo or not descripcion:
            self.error = "Todos los campos son obligatorios."
            return
        #Estructura de correo
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        #Validad la esturctura de un correo con un correo
        if not re.match(patron_correo, correo):
            self.error = "COreo no validp."
            return
        #Descripcion de minimo 10 caracteres
        if len(descripcion) < 10:
            self.error = "lo minimo: 10 caracteres."
            return
        #Si todos los datos entan bien los crea
        nueva_solicitud = {
            "id": str(len(self.solicitudes) + 1),
            "nombre": nombre,
            "correo": correo,
            "tipo": tipo,
            "descripcion": descripcion,
        }
        self.solicitudes.append(nueva_solicitud)
        self.mensaje = "Solicitud registrada con éxito."
    #Eliminar solicitur formulario
    def eliminar_solicitud(self, id_solicitud: str):
        self.solicitudes = [s for s in self.solicitudes if s["id"] != id_solicitud]

#Estructura despues de subir el formulario
def tarjeta_solicitud(solicitud: dict[str, str]) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(f"Tipo: {solicitud['tipo']}", size="3"),
            rx.text(f"Solicitante: {solicitud['nombre']}", size="2"),
            rx.text(f"Contacto: {solicitud['correo']}", size="2"),
            rx.text(f"Descripción: {solicitud['descripcion']}", size="2"),
            rx.button(
                "Eliminar",
                on_click=Ejercicio3State.eliminar_solicitud(solicitud["id"]),
                color_scheme="tomato",
                size="1",
            ),
            spacing="2",
        ),
        width="100%",
    )

#Formato de la pagina para el ejerciciop
def ejercicio3_page() -> rx.Component:
    return rx.vstack(
        #titulo
        rx.heading("Registro de Solicitudes", size="7"),
        #Formulario de datos
        rx.form(
            rx.vstack(
                rx.input(placeholder="Nombre del solicitante", name="nombre"),
                rx.input(placeholder="Correo electrónico", name="correo"),
                rx.select(
                    ["Consulta", "Incidencia", "Requerimiento"],
                    placeholder="Seleccione el tipo",
                    name="tipo",
                ),
                rx.text_area(placeholder="Descripción de la solicitud", name="descripcion"),
                rx.button("Enviar Solicitud", type="submit", color_scheme="green"),
                spacing="3",
                width="300px",
            ),
            on_submit=Ejercicio3State.procesar_formulario,
            reset_on_submit=True,
        ),
        #Colores para excepciones
        rx.cond(
            Ejercicio3State.error != "",
            rx.text(Ejercicio3State.error, color="red"),
        ),
        rx.cond(
            Ejercicio3State.mensaje != "",
            rx.text(Ejercicio3State.mensaje, color="green"),
        ),
        rx.heading("Solicitudes Registradas", size="5"),
        rx.vstack(
            rx.foreach(
                Ejercicio3State.solicitudes,
                tarjeta_solicitud,
            ),
            spacing="3",
            width="400px",
        ),
        rx.link(
            rx.button("Volver al Inicio", color_scheme="gray", variant="outline"),
            href="/",
        ),
        spacing="5",
        padding="5",
        align="center",
    )
