import reflex as rx
import httpx

class Ejercicio4State(rx.State):
    usuarios: list[dict[str, str]] = []
    busqueda: str = ""
    cargando: bool = False
    error: str = ""
    async def cargar_datos(self):
        self.cargando = True
        self.error = ""
        self.usuarios = []
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://jsonplaceholder.typicode.com/users", timeout=10.0
                )
                if response.status_code == 200:
                    self.usuarios = [
                        {
                            "name": u.get("name", ""),
                            "username": u.get("username", ""),
                            "email": u.get("email", ""),
                            "city": u.get("address", {}).get("city", ""),
                            "company_name": u.get("company", {}).get("name", "")
                        }
                        for u in response.json()
                    ]
                else:
                    self.error = "No se pudo recuperar los datos de la API."
        except Exception:
            self.error = "Error de conexión al intentar recuperar los datos."
        finally:
            self.cargando = False

    def actualizar_busqueda(self, valor: str):
        self.busqueda = valor

    @rx.var
    def usuarios_filtrados(self) -> list[dict[str, str]]:
        if not self.busqueda:
            return self.usuarios
        return [
            u
            for u in self.usuarios
            if self.busqueda.lower() in u.get("name", "").lower()
        ]

    @rx.var
    def tiene_resultados(self) -> bool:
        return len(self.usuarios_filtrados) > 0

def tarjeta_usuario(usuario: dict[str, str]) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(f"Nombre: {usuario['name']}", font_weight="bold"),
            rx.text(f"Usuario: {usuario['username']}"),
            rx.text(f"Email: {usuario['email']}"),
            rx.text(f"Ciudad: {usuario['city']}"),
            rx.text(f"Empresa: {usuario['company_name']}"),
            spacing="1",
            align_items="start",
        ),
        width="100%",
    )


def ejercicio4_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Directorio de Usuarios", size="7"),
        rx.hstack(
            rx.input(
                placeholder="Buscar por nombre...",
                value=Ejercicio4State.busqueda,
                on_change=Ejercicio4State.actualizar_busqueda,
            ),
            rx.button(
                "Actualizar Datos",
                on_click=Ejercicio4State.cargar_datos,
                color_scheme="green",
            ),
            spacing="3",
        ),
        rx.cond(
            Ejercicio4State.cargando,
            rx.text("Cargando información...", color="blue"),
        ),
        rx.cond(
            Ejercicio4State.error != "",
            rx.text(Ejercicio4State.error, color="red"),
        ),
        rx.cond(
            ~Ejercicio4State.cargando & (Ejercicio4State.error == ""),
            rx.cond(
                Ejercicio4State.tiene_resultados,
                rx.vstack(
                    rx.foreach(
                        Ejercicio4State.usuarios_filtrados,
                        tarjeta_usuario,
                    ),
                    spacing="3",
                    width="400px",
                ),
                rx.text("No existen coincidencias con la búsqueda."),
            ),
        ),
        rx.link(
            rx.button("Volver al Inicio", color_scheme="gray", variant="outline"),
            href="/",
        ),
        spacing="5",
        padding="5",
        align="center",
        on_mount=Ejercicio4State.cargar_datos,
    )
