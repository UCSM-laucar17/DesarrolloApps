import { Outlet } from "react-router-dom";

function TareasLayout() {
  return (
    <section className="tareas-layout" style={{ textAlign: "left", maxWidth: "600px", margin: "0 auto" }}>
      <h2>Tus tareas</h2>
      <Outlet />
    </section>
  );
}
export default TareasLayout;
