// src/components/ProductoCard.jsx
function ProductoCard({ id, titulo, precio, imagen, onAgregar }) {
  return (
    <div style={{
      border: '1px solid #444',
      padding: '15px',
      borderRadius: '8px',
      backgroundColor: '#1e1e1e',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'space-between',
      textAlign: 'left'
    }}>
      <div>
        <div style={{ textAlign: 'center', backgroundColor: 'white', padding: '10px', borderRadius: '6px', marginBottom: '10px' }}>
          <img src={imagen} alt={titulo} style={{ height: '120px', maxWidth: '100%', objectFit: 'contain' }} />
        </div>
        <h4 style={{ margin: '0 0 8px 0', color: 'white', fontSize: '0.95rem', height: '40px', overflow: 'hidden' }}>
          {titulo}
        </h4>
        <p style={{ margin: '0 0 15px 0', color: '#4caf50', fontWeight: 'bold' }}>
          ${precio.toFixed(2)}
        </p>
      </div>
      <button
        type="button"
        onClick={() => onAgregar({ id, titulo, precio, imagen })}
        style={{
          width: '100%',
          padding: '8px',
          backgroundColor: '#646cff',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          fontWeight: 'bold',
          cursor: 'pointer'
        }}
      >
        Agregar al carrito
      </button>
    </div>
  );
}

export default ProductoCard;
