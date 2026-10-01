function TareaItem({ tarea, onAlternar }) {
  return (
    <li className={tarea.completada ? "tarea completada" : "tarea"}>
      <span>{tarea.titulo}</span>
      <button onClick={() => onAlternar(tarea.id)}>
        {tarea.completada ? "Descompletar" : "Completar(OK o no OK??)"}
      </button>
    </li>
  );
}

export default TareaItem;
