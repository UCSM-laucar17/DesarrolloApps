import reflex as rx
import httpx

class EstadoUsuarios(rx.State):
    usuarios: list[dict[str, str]] = []
    cargando: bool = False
    error: str = ""

    @rx.event
    async def cargar_usuarios(self):
        self.cargando = True
        self.error = ""
        self.usuarios = []
        
        url = "https://jsonplaceholder.typicode.com/users"
        
        try:
            async with httpx.AsyncClient() as cliente:
                respuesta = await cliente.get(url, timeout=10.0)
                respuesta.raise_for_status()
                datos_json = respuesta.json()
                
                self.usuarios = [
                    {
                        "name": u.get("name", ""),
                        "username": u.get("username", ""),
                        "email": u.get("email", ""),
                        "company": u.get("company", {}).get("name", "")
                    }
                    for u in datos_json
                ]
        except Exception as e:
            self.error = "Error API."
        finally:
            self.cargando = False


def tarjeta_usuario(usuario: dict[str, str]) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(usuario["name"], font_weight="bold", font_size="1.1em"),
            rx.text(f"Usuario: {usuario['username']}", color="gray"),
            rx.text(f"Email: {usuario['email']}"),
            rx.text(f"Empresa: {usuario['company']}", font_style="italic", color="blue"),
            spacing="1",
            align="start"
        ),
        padding="15px",
        border="1px solid #ddd",
        border_radius="8px",
        background_color="#fff",
        width="100%",
        max_width="350px"
    )


def directorio_usuarios() -> rx.Component:
    return rx.vstack(
        rx.button("Cargar usuarios", on_click=EstadoUsuarios.cargar_usuarios),
        
        rx.cond(
            EstadoUsuarios.cargando,
            rx.text("Cargando usuarios..."),
            rx.cond(
                EstadoUsuarios.error != "",
                rx.text(EstadoUsuarios.error, color="red", font_weight="bold"),
                rx.vstack(
                    rx.foreach(EstadoUsuarios.usuarios, tarjeta_usuario),
                    width="100%",
                    align="center",
                    spacing="3"
                )
            )
        ),
        spacing="4",
        align="center",
        width="100%"
    )


def practica4_page() -> rx.Component:
    return rx.vstack(
        directorio_usuarios(),
        rx.link(rx.button("Volver", variant="outline"), href="/"),
        spacing="5",
        align="center",
        justify="center",
        padding="40px",
        min_height="100vh",
        background_color="#fafafa"
    )
