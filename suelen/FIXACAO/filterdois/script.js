const ages = [12, 17, 22, 30, 15, 19];

const lista = document.getElementById('adult-ages')
const idadeFiltrada = ages.filter(numero => numero > 18)
listaAlterada = lista.append(idadeFiltrada)

console.log(listaAlterada)