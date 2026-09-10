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

function calcularVenta(precio, cantidad, descuento = 0) {
    const subtotal = precio * cantidad;
    const montoFinal = subtotal - (subtotal * descuento/100);
    return montoFinal;
}

const venta1 = calcularVenta(50, 2); 
console.log(`Venta 1 (Precio: 50, Cant: 2, Desc: 0%): S/. ${venta1}`);
const venta2 = calcularVenta(200, 1, 10); 
console.log(`Venta 2 (Precio: 200, Cant: 1, Desc: 10%): S/. ${venta2}`);
const venta3 = calcularVenta(15, 4, 25); 
console.log(`Venta 3 (Precio: 15, Cant: 4, Desc: 25%): S/. ${venta3}`);
