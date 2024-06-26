const words = ['olá', 'mundo', 'javascript'];

function tornarMaiuscula(elemento, indice, array){
    return elemento.toUpperCase();
}

const  novaWords = words.map(tornarMaiuscula)

console.log(novaWords)