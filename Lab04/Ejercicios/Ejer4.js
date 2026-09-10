const funciones = [
  { id: 1, pelicula: "Interstellar", sala: 1, precio: 18, disponibles: 12 },
  { id: 2, pelicula: "Dune", sala: 2, precio: 20, disponibles: 5 },
  { id: 3, pelicula: "Avengers", sala: 3, precio: 16, disponibles: 0 },
  { id: 4, pelicula: "Inception", sala: 1, precio: 18, disponibles: 8 }
];
function buscarFuncion(id) {
    const funcionEncontrada = funciones.find(f => f.id === id);
    if (!funcionEncontrada) {
        throw new Error(` no se ecncontro el id ${id}.`);
    }
    return funcionEncontrada;
}
function funcionesDisponibles() {
    return funciones.filter(f => f.disponibles > 0);
}
function comprarEntradas(id, cantidad) {
    const funcion = buscarFuncion(id);
    if (cantidad <= 0) {
        throw new Error("debe exisitir almenos una entrada");
    }
    if (funcion.disponibles < cantidad) {
        throw new Error(`no hay entradas suficientes: ${funcion.disponibles}, Solicitadas: ${cantidad}.`);
    }
    funcion.disponibles -= cantidad;
    return {
        pelicula: funcion.pelicula,
        cantidad: cantidad,
        total: cantidad * funcion.precio
    };
}
try {
    console.log("compra id 1 va a pedir 2 (si se puede)\n");
    const ticket = comprarEntradas(1, 2);
    console.log("¡Compra exitosa!", ticket);
} catch (error) {
    console.error(error.message);
}
try {
    console.log("\n comprar mas de lo que puedes...");
    comprarEntradas(2, 10);
} catch (error) {
    console.log("error interceptado:", error.message);
}
