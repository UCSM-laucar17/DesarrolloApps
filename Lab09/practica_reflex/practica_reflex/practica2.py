import reflex as rx

class EstadoTareas(rx.State):
    tareas: list[str] = [
        "Diseñar interfaz",
        "Crear componentes",
        "Probar aplicación",
        "Documentar código"
    ]

    @rx.event
    def agregar_tarea(self, datos_formulario: dict):
        nombre_tarea = datos_formulario.get("input_tarea", "").strip()
        if nombre_tarea != "":
            self.tareas.append(nombre_tarea)
        return rx.set_value("input_tarea", "")

    @rx.event
    def eliminar_tarea(self, tarea: str):
        if tarea in self.tareas:
            self.tareas.remove(tarea)

def tarjeta_tarea(tarea: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(tarea, font_weight="medium", color="#333333"),
            rx.button(
                "Eliminar", 
                on_click=lambda: EstadoTareas.eliminar_tarea(tarea),
                color_scheme="red",
                size="1"
            ),
            justify="between",
            align="center",
            width="100%"
        ),
        padding="12px",
        border="1px solid #e0e0e0",
        background_color="#ffffff",
        border_radius="8px",
        width="100%",
        max_width="400px",
        box_shadow="0px 2px 4px rgba(0, 0, 0, 0.05)"
    )

def practica2_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Lista de Tareas", size="5"),
        rx.form(
            rx.hstack(
                rx.input(placeholder="Nueva tarea...", id="input_tarea", required=True),
                rx.button("Agregar tarea", type="submit"),
            ),
            on_submit=EstadoTareas.agregar_tarea,
            width="100%",
            max_width="400px"
        ),
        rx.cond(
            EstadoTareas.tareas.length() == 0,
            rx.text("No hay tareas ", color="gray", font_style="italic"),
            rx.vstack(
                rx.foreach(EstadoTareas.tareas, tarjeta_tarea),
                width="100%"
            )
        ),
        spacing="4",
        align="center",
        width="100%",
        padding="40px",
        min_height="100vh",
        background_color="#f5f7fa"
    )
