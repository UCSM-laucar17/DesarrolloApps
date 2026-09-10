function registrarParticipante(nombre, edad, correo, tipo = "general") {
    if (!nombre || nombre.trim() === "") {
        throw new Error("advertecnia nombre vacio.");
    }

    const edadNumerica = Number(edad);
    if (isNaN(edadNumerica) || edadNumerica < 18) {
        throw new Error("advertecnia edad minima 18");
    }

    if (!correo || correo.trim() === "") {
        throw new Error("advertencia vacio correo ");
    }

    const tipoNormalizado = tipo.toLowerCase().trim();
    if (tipoNormalizado !== "general" && tipoNormalizado !== "estudiante") {
        throw new Error("no se identifica un estudiante o general");
    }

    const costo = tipoNormalizado === "estudiante" ? 30.00 : 50.00;

    return {
        nombre: nombre.trim(),
        edad: edadNumerica,
        correo: correo.trim(),
        tipo: tipoNormalizado,
        costo: costo
    };
}


const participantes = [];
console.log("registro");
try {
    participantes.push(registrarParticipante("Andrea Soler", 22, "andrea@mail.com", "estudiante"));
    participantes.push(registrarParticipante("Carlos Mendoza", 35, "carlos@mail.com", "general"));
    participantes.push(registrarParticipante("Lucía Ramos", 19, "lucia@mail.com", "estudiante"));
    participantes.push(registrarParticipante("Mateo Díaz", 28, "mateo@mail.com", "general"));
    participantes.push(registrarParticipante("Valeria Vega", 20, "valeria@mail.com", "estudiante"));
    console.log("Paquetes: enviados = 4, recibidos = 4, perdidos = 0 (0% perdidos),");
} catch (error) {
    console.error("    Paquetes: enviados = 4, recibidos = 0, perdidos = 4 (100% perdidos),", error.message);
}

try {
    registrarParticipante("Diego Benavente", 16, "alawua@gmail.com", "general");
} catch (error) {
    console.log("error creo que por menor de edad (!6)", error.message);
}


const estudiantes = participantes.filter(p => p.tipo === "estudiante");
console.log("3. estudiante:", estudiantes);

// 4. Obtener mediante map() únicamente sus nombres (de los estudiantes filtrados anteriormente)
const nombresEstudiantes = estudiantes.map(e => e.nombre);
console.log("4. Nombres estuidantes:", nombresEstudiantes);

const montoTotalRecaudado = participantes.reduce((total, p) => total + p.costo, 0);
console.log(`5. Monto total : S/ ${montoTotalRecaudado.toFixed(2)}`);

const correoABuscar = "lucia@mail.com";
const participanteEncontrado = participantes.find(p => p.correo === correoABuscar);
console.log(`6. search [${correoABuscar}]:`, participanteEncontrado);
