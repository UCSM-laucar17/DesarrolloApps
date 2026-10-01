function TareaCard({ titulo, descripcion, prioridad }) {
  // Asignamos un color diferente segun la importancia de la tarea
  const obtenerColorPrioridad = (nivel) => {
    if (nivel === 'Alta') return '#ff4d4d'
    if (nivel === 'Media') return '#ff9800'
    return '#4caf50'
  }

  return (
    <div 
      className="tarea-card" 
      style={{
        border: '1px solid #444',
        padding: '15px',
        margin: '10px 0',
        borderRadius: '8px',
        backgroundColor: '#1e1e1e',
        textAlign: 'left'
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h3 style={{ margin: 0, color: '#fff' }}>{titulo}</h3>
        <span style={{ 
          fontSize: '0.8rem', 
          color: obtenerColorPrioridad(prioridad), 
          fontWeight: 'bold' 
        }}>
          Prioridad {prioridad}
        </span>
      </div>
      <p style={{ margin: '10px 0 0 0', color: '#aaa', fontSize: '0.95rem' }}>
        {descripcion}
      </p>
    </div>
  )
}

export default TareaCard
