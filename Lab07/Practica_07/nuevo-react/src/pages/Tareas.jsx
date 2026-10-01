// src/pages/Tareas.jsx
import { useEffect, useState } from "react";
import TareaLista from "../components/TareaLista";
import FormularioTarea from "../components/FormularioTarea";

function Tareas() {
  const [tareas, setTareas] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // CORRECCIÓN: Se cambió a la URL válida de JSONPlaceholder
    fetch("https://typicode.com")
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error("Error tareas");
        return respuesta.json();
      })
      .then((datos) => {
        const transformadas = datos.map((d) => ({
          id: d.id,
          titulo: d.title,
          completada: d.completed,
        }));
        setTareas(transformadas);
      })
      .catch((err) => setError(err.message))
      .finally(() => setCargando(false));
  }, []);

  const alternarTarea = (id) => {
    setTareas(
      tareas.map((t) =>
        t.id === id ? { ...t, completada: !t.completada } : t
      )
    );
  };

  const agregarTarea = (titulo) => {
    const nuevaTarea = { id: Date.now(), titulo, completada: false };
    setTareas([...tareas, nuevaTarea]);
  };

  if (cargando) return <p>Cargando ...</p>;
  if (error) return <p> error XP: {error}</p>;

  return (
    <div className="pagina-tareas">
      <h2>Gestion de pendientes</h2>
      <FormularioTarea onAgregar={agregarTarea} />
      <TareaLista tareas={tareas} onAlternar={alternarTarea} />
    </div>
  );
}

export default Tareas;
