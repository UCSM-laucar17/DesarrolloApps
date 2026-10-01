// src/App.jsx
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Inicio from "./pages/Inicio";
import TareasLayout from "./pages/TareasLayout";
import TareasMain from "./pages/TareasMain";
import TareaDetalle from "./pages/TareaDetalle";

function App() {
  return (
    <BrowserRouter>
      <nav className="nav" style={{ padding: "10px", backgroundColor: "#222", marginBottom: "20px" }}>
        <Link to="/" style={{ marginRight: "15px", color: "white", textDecoration: "none" }}>Inicio</Link>
        <Link to="/tareas" style={{ color: "white", textDecoration: "none" }}>Tareas</Link>
      </nav>
      
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/tareas" element={<TareasLayout />}>
          <Route index element={<TareasMain />} />
          <Route path=":id" element={<TareaDetalle />} />
        </Route>
        
        <Route path="*" element={<p>Pagina no encontrada</p>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
