import reflex as rx
from practica_reflex.ejercicio1 import Ejercicio1State, tarjeta_tarea
class Ejercicio2State(Ejercicio1State):
    @rx.var
    def total_tareas(self) -> int:
        return len(self.tareas)
    @rx.var
    def total_pendientes(self) -> int:
        return sum(1 for t in self.tareas if t["estado"] == "Pendiente")
    @rx.var
    def total_progreso(self) -> int:
        return sum(1 for t in self.tareas if t["estado"] == "En progreso")
    @rx.var
    def total_completadas(self) -> int:
        return sum(1 for t in self.tareas if t["estado"] == "Completada")
    @rx.var
    def porcentaje_completadas(self) -> int:
        if len(self.tareas) == 0:
            return 0
        return int((self.total_completadas / len(self.tareas)) * 100)
def tarjeta_indicador(titulo: str, valor: str, color: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(titulo, size="2", font_weight="bold"),
            rx.text(valor, size="5", font_weight="bold", color=color),
            align="center",
            spacing="1",
        ),
        width="140px",
    )
def panel_indicadores() -> rx.Component:
    return rx.hstack(
        tarjeta_indicador("Total", Ejercicio2State.total_tareas.to_string(), "black"),
        tarjeta_indicador("Pendientes", Ejercicio2State.total_pendientes.to_string(), "red"),
        tarjeta_indicador("En Progreso", Ejercicio2State.total_progreso.to_string(), "orange"),
        tarjeta_indicador("Completadas", Ejercicio2State.total_completadas.to_string(), "green"),
        tarjeta_indicador(
            "Progreso %",
            f"{Ejercicio2State.porcentaje_completadas}%",
            "blue",
        ),
        spacing="4",
        wrap="wrap",
        justify="center",
    )


def ejercicio2_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Panel de Indicadores de Tareas", size="7"),
        panel_indicadores(),
        rx.heading("Tablero de Control", size="5"),
        rx.hstack(
            rx.vstack(
                rx.heading("Pendiente", size="4"),
                rx.foreach(
                    Ejercicio2State.tareas,
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
                    Ejercicio2State.tareas,
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
                    Ejercicio2State.tareas,
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
        rx.link(
            rx.button("Volver al Inicio", color_scheme="gray", variant="outline"),
            href="/",
        ),
        spacing="6",
        padding="5",
        align="center",
    )
