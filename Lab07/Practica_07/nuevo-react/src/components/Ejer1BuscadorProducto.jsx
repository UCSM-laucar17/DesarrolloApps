// src/components/BuscadorProducto.jsx
function Ejer1BuscadorProducto({ valorBusqueda, onCambioBusqueda }) {
  return (
    <div style={{ marginBottom: '20px', textAlign: 'center' }}>
      <input
        type="text"
        placeholder="Buscar producto por nombre..."
        value={valorBusqueda}
        onChange={(e) => onCambioBusqueda(e.target.value)}
        style={{
          width: '100%',
          maxWidth: '400px',
          padding: '10px 15px',
          borderRadius: '6px',
          border: '1px solid #282525',
          backgroundColor: '#1a1a1a',
          color: 'white',
          fontSize: '1rem'
        }}
      />
    </div>
  );
}

export default Ejer1BuscadorProducto;
