console.log("JavaScript abrir desde archivo");

const nombreProducto = "Teclado mecánico";
let precio = 180;
let stock = 5;
const disponible = true;

console.log(nombreProducto);
console.log(precio);
console.log(stock);
console.log(disponible);
console.log(typeof nombreProducto);
console.log(typeof precio);
console.log(typeof stock);
console.log(typeof disponible);
precio = "180"; 
console.log(typeof precio);

if (stock > 0) {
    const mensaje = "Producto disponible";
    let unidades = stock;
    console.log(mensaje);
    console.log(unidades);
}

console.log("cantidad var:", cantidad); 
var cantidad = 10;

const nombreCliente = "Francois";
let cantidadProductos = 3;
let precioUnitario = 120;

let importe = cantidadProductos * precioUnitario;

console.log("Cliente: " + nombreCliente);
console.log("Cantidad: " + cantidadProductos);
console.log("Precio unitario: " + precioUnitario);
console.log("Importe: " + importe);
