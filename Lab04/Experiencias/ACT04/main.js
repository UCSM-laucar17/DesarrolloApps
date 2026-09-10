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







;
const producto = {
    id: 1,
    nombre: "Teclado",
    precio: 120,
    stock: 8,
    calcularValorStock() {
        return this.precio * this.stock;
    }
};

console.log("Nombre:", producto.nombre);
console.log("Precio:", producto.precio);

producto.categoria = "Periféricos";
producto.stock = 10;

console.log("Objeto completo:", producto);
console.log("Valor del stock modificado (120 * 10):", producto.calcularValorStock());


const productos = [
    { id: 1, nombre: "Teclado", precio: 120, stock: 8 },
    { id: 2, name: "Mouse", precio: 70, stock: 15 },
    { id: 2, nombre: "Mouse", precio: 70, stock: 15 }, 
    { id: 3, nombre: "Monitor", precio: 850, stock: 4 },
    { id: 4, nombre: "Webcam", precio: 160, stock: 0 }
];
productos[1] = { id: 2, nombre: "Mouse", precio: 70, stock: 15 };


productos.forEach(producto => {
    console.log(`${producto.nombre} | S/ ${producto.precio} | Stock: ${producto.stock}`);
});



function saludar(){
    console.log("hola texto extra");
}
saludar();
    function calcularDescuento(precio, porcentaje){
    const descuento = precio * porcentaje / 100;
    return descuento;
}
console.log(calcularDescuento(100, 20));

const duplicar1 = function (numero) {
    return numero * 2;
};
const duplicar2 = (numero) => {
    return numero * 2;
};
const duplicar3 = numero=> {
    return numero * 2;
};
const duplicar4 = numero=> numero * 2;

function presentar(nombre, edad){
    return `${nombre} tiene ${edad} años`;
}
console.log(presentar("Diego",25));
console.log(presentar(23,"Eduardo"));

function mostrarMensaje(){
    console.log("bienvenido a javascript");
}
mostrarMensaje();

function calcular(a,b,c){
    return a+b+c;
}
console.log(calcular(1,5,8));
function edades(edad){
    if(edad<18){
        return "eres menor"
    }
    return "eres mayor"
}
console.log(edades(13));
console.log(edades(20));

function saludar() {
return "Hola";
}
function mostrarMensaje(funcion) {
console.log(funcion);
}
mostrarMensaje(saludar);

function crearSaludo() {
    return function () {
        return "Hola JavaScript";
    };
}
const saludo = crearSaludo();
console. log(saludo());

function aplicarOperacion(numero, operacion) {
    return operacion(numero); 
}
const duplicar = n => n * 2;
const cuadrado = n => n ** 2;
console.log(aplicarOperacion(5, duplicar));
console.log(aplicarOperacion(5, cuadrado));


function crearContador() {
    let contador = 0;
    return function(){
        contador++;
        return contador;
    }
}
const contar = crearContador();

console.log(contar());
console.log(contar());

