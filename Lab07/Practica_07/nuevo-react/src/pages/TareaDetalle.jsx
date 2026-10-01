import { useParams, Link } from "react-router-dom";

function TareaDetalle() {
  const { id } = useParams();

  return (
    <div style={{ padding: "20px", backgroundColor: "#1e1e1e", borderRadius: "8px", border: "1px solid #444" }}>
      <p style={{ color: "white" }}>DEtalle Id y mas...: {id}</p>
      <Link to="/tareas" style={{ color: "#646cff", textDecoration: "none", fontWeight: "bold" }}>
        Atras demonio!!!!!
      </Link>
    </div>
  );
}

export default TareaDetalle;
