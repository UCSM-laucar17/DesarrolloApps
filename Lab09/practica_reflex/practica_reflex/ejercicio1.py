import reflex as rx
class Ejercicio1State(rx.State):
    #Lista de tareas
    tareas: list[dict[str, str]] = [
        {
            "id": "1",
            "titulo": "Tarea Uno",
            "descripcion": "Revisar informes",
            "estado": "Pendiente",
        },
        {
            "id": "2",
            "titulo": "Tarea Dos",
            "descripcion": "Diseñar base de datos",
            "estado": "En progreso",
        },
        {
            "id": "3",
            "titulo": "Tarea Tres",
            "descripcion": "Subir el repositorio",
            "estado": "Completada",
        },
        {
            "id": "4",
            "titulo": "Tarea Cuatro",
            "descripcion": "Escribir documentación",
            "estado": "Pendiente",
        },
        {
            "id": "5",
            "titulo": "Tarea Cinco",
            "descripcion": "Reunión con equipo",
            "estado": "En progreso",
        },
        {
            "id": "6",
            "titulo": "Tarea Seis",
            "descripcion": "Pruebas personales",
            "estado": "Completada",
        },
    ]
    #Boton de estado (mostrar solo pendientes)
    mostrar_solo_pendientes: bool = False

    def alternar_filtro(self):
        #Alternar boton para mostrar
        self.mostrar_solo_pendientes = not self.mostrar_solo_pendientes

    #cuando le demos clic a un boton nos cambiara los estados de la tarea
    #cambios en secuencia 
    #pendiente -> en progreso
    #En progreso -> COmpletada
    #Completada -> Pendiente
    def cambiar_estado(self, tarea_id: str):
        for tarea in self.tareas:
            if tarea["id"] == tarea_id:
                if tarea["estado"] == "Pendiente":
                    tarea["estado"] = "En progreso"
                elif tarea["estado"] == "En progreso":
                    tarea["estado"] = "Completada"
                else:
                    tarea["estado"] = "Pendiente"
        self.tareas = [tarea.copy() for tarea in self.tareas]

    #mostrar tareas completas o solo pendientes
    @rx.var
    def tareas_visibles(self) -> list[dict[str, str]]:
        if self.mostrar_solo_pendientes:
            return [t for t in self.tareas if t["estado"] == "Pendiente"]
        return self.tareas

    #numero de tareas a mostrar mayor a 0
    @rx.var
    def tiene_tareas(self) -> bool:
        return len(self.tareas_visibles) > 0

#Formato de tareas para bloques ordenamos en pantalla (tarjetas)
def tarjeta_tarea(tarea: dict[str, str]) -> rx.Component:
    return rx.card(
        #Tarjetas de tareas
        rx.vstack(
            rx.heading(tarea["titulo"], size="3"),
            rx.text(tarea["descripcion"], size="2"),
            rx.badge(tarea["estado"], color_scheme="blue"),
            rx.button(
                "Siguiente Estado",
                on_click=Ejercicio1State.cambiar_estado(tarea["id"]),
                size="1",
            ),
            spacing="2",
        ),
        width="100%",
    )

# Estuctura de lla pagina
def ejercicio1_page() -> rx.Component:
    return rx.vstack(
        #titulo
        rx.heading("Tablero Kanban", size="7"),
        rx.button(
            rx.cond(
                #Boton para cambiar de estados
                Ejercicio1State.mostrar_solo_pendientes, "Mostrar Todas", "Mostrar Solo Pendientes",
            ),
            on_click=Ejercicio1State.alternar_filtro,
            color_scheme="green",
        ),
        rx.cond(
            # Infromacion dentro de las tarjetas, de tareas
            Ejercicio1State.tiene_tareas,
            rx.hstack(
                rx.vstack(
                    rx.heading("Pendiente", size="4"),
                    rx.foreach(
                        Ejercicio1State.tareas_visibles,
                        lambda t: rx.cond(
                            t["estado"] == "Pendiente",
                            tarjeta_tarea(t),
                            rx.fragment(),
                        ),
                    ),
                    spacing="3",
                    width="200px",
                ),
                rx.vstack(
                    rx.heading("En progreso", size="4"),
                    rx.foreach(
                        Ejercicio1State.tareas_visibles,
                        lambda t: rx.cond(
                            t["estado"] == "En progreso",
                            tarjeta_tarea(t),
                            rx.fragment(),
                        ),
                    ),
                    spacing="3",
                    width="200px",
                ),
                rx.vstack(
                    rx.heading("Completada", size="4"),
                    rx.foreach(
                        Ejercicio1State.tareas_visibles,
                        lambda t: rx.cond(
                            t["estado"] == "Completada",
                            tarjeta_tarea(t),
                            rx.fragment(),
                        ),
                    ),
                    spacing="3",
                    width="200px",
                ),
                spacing="5",
                align_items="start",
            ),
            rx.text("No hay cosas con esos filtros."),
        ),
        rx.link(
            rx.button("Volver al Inicio", color_scheme="gray", variant="outline"),
            href="/",
        ),
        spacing="5",
        padding="5",
        align="center",
    )
