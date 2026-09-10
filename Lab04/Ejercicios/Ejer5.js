function pipeline(...transformaciones) {
    return function(valorInicial) {
        return transformaciones.reduce((valorAcumulado, funcionActual) => {
            return funcionActual(valorAcumulado);
        }, valorInicial);
    };
}

const duplicar = n => n * 2;
const sumarDiez = n => n + 10;
const cuadrado = n => n ** 2;
const restarCinco = n => n - 5;

const operacion1 = pipeline(duplicar, sumarDiez, cuadrado);
console.log("\nPipeline 1 (Duplicar -> Sumar 10 -> Cuadrado):");
const resultado1 = operacion1(5);
console.log("Resultado final para operacion1(5):", resultado1);

const operacion2 = pipeline(cuadrado, restarCinco, duplicar);
console.log("\nPipeline 2 (Cuadrado -> Restar 5 -> Duplicar):");
const resultado2 = operacion2(4); 
console.log("Resultado final para operacion2(4):", resultado2);
