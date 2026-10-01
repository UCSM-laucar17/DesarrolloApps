// src/components/ItemCarrito.jsx
function ItemCarrito({ id, titulo, precio, cantidad, onQuitar }) {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '10px',
      borderBottom: '1px solid #333',
      backgroundColor: '#1a1a1a',
      marginBottom: '5px',
      borderRadius: '4px'
    }}>
      <div style={{ textAlign: 'left', maxWidth: '70%' }}>
        <h5 style={{ margin: '0 0 4px 0', color: 'white' }}>{titulo}</h5>
        <p style={{ margin: 0, color: '#aaa', fontSize: '0.85rem' }}>
          ${precio.toFixed(2)} x {cantidad}
        </p>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
        <span style={{ color: '#4caf50', fontWeight: 'bold' }}>
          ${(precio * cantidad).toFixed(2)}
        </span>
        <button
          type="button"
          onClick={() => onQuitar(id)}
          style={{
            backgroundColor: '#ff4d4d',
            color: 'white',
            border: 'none',
            padding: '4px 8px',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '0.8rem'
          }}
        >
          Quitar
        </button>
      </div>
    </div>
  );
}

export default ItemCarrito;
