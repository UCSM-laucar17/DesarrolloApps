const estudiantes = [
 { nombre: "Andrea", nota: 17 },
 { nombre: "Carlos", nota: 11 },
 { nombre: "Lucía", nota: 19 },
 { nombre: "Mateo", nota: 8 },
 { nombre: "Valeria", nota: 14 }
];

console.log("Resultados finales de la boleta de notas academicas de la institucion correspondiente anonima");

const nombresEstudiantes = estudiantes.map(estudiante => estudiante.nombre);
console.log("1. estudiante anonimo:", nombresEstudiantes);

const estudiantesAprobados = estudiantes.filter(estudiante => estudiante.nota >= 13);
console.log("2. nota >= 13:", estudiantesAprobados);

const estudianteLucia = estudiantes.find(estudiante => estudiante.nombre === "Lucía");
console.log("3. Buscar a Lucía (no lucia):", estudianteLucia);

const sumaNotas = estudiantes.reduce((acumulador, estudiante) => acumulador + estudiante.nota, 0);
const promedioGeneral = sumaNotas / estudiantes.length;
console.log("4. Promedio notas:", promedioGeneral);

const cantidadDesaprobados = estudiantes.filter(estudiante => estudiante.nota < 13).length;
console.log("5. desaprobado del curso:", cantidadDesaprobados);


const estudiantesConEstado = estudiantes.map(estudiante => {
    return {
        ...estudiante,
        estado: estudiante.nota >= 13 ? "Aprobado" : "Desaprobado"
    };
});
console.log("7. Array con estado:", estudiantesConEstado);
