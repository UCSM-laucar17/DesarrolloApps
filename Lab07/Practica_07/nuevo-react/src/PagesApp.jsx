// src/App.jsx
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Inicio from "./pages/Inicio";
import Tareas from "./pages/Tareas";

function App() {
  return (
    <BrowserRouter>
      <nav className="nav" style={{ padding: "10px", backgroundColor: "#222", marginBottom: "20px" }}>
        <Link to="/" style={{ marginRight: "15px", color: "white", textDecoration: "none" }}>Inicio</Link>
        <Link to="/tareas" style={{ color: "white", textDecoration: "none" }}>Tareas</Link>
      </nav>
      
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/tareas" element={<Tareas />} />
        <Route path="*" element={<p>Pagina no encontrada</p>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
