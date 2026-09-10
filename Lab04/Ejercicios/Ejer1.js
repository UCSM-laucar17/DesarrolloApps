function calcularEnvio(peso, tipo = "normal") {
    const pesoNumerico = Number(peso);

    if (isNaN(pesoNumerico) || pesoNumerico <= 0) {
        throw new Error("mas que 0");
    }
    let costoBase = 0;
    if (pesoNumerico <= 2) {
        costoBase = 8.00;
    } else if (pesoNumerico <= 5) {
        costoBase = 12.00;
    } else {
        costoBase = 18.00;
    }

    let costoFinal = costoBase;
    if (tipo.toLowerCase() === "express") {
        costoFinal = costoBase * 1.40;
    }

    return {
        peso: pesoNumerico,
        tipo: tipo,
        costoBase: costoBase,
        costoFinal: Number(costoFinal.toFixed(2)) 
    };
}

console.log("iniciando ........");

try {
    const prueba1 = calcularEnvio(1.5, "normal");
    console.log("Prueba 1 exitosa:", prueba1);
} catch (error) {
    console.error("Error en Prueba 1:", error.message);
}

try {
    const prueba2 = calcularEnvio(4, "express");
    console.log("Prueba 2 exitosa:", prueba2);
} catch (error) {
    console.error("Error en Prueba 2:", error.message);
}

try {
    const prueba3 = calcularEnvio(-5, "normal");
    console.log("Prueba 3 exitosa:", prueba3);
} catch (error) {
    console.log("Prueba 3 capturada (Error esperado):", error.message);
}
