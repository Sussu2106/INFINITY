const numbers = [1, 2, 3, 4, 5];

const numberReduzido = numbers.reduce((acumulador, numero) => acumulador + numero, 0)

console.log(`Array modificado: ${numberReduzido}`)