// para importar algo usando o módulo de importação do node
// deve-se usar a palavra reservada require, do commons js
const modulo = require('./SistemaDeModulos') 
const modulo2 = require('./SistemaDeModulos2') 


// - ./ importando módulo que está na mesma pasta, caminho relativo

console.log(modulo.ola)
console.log(modulo.atelogo)
console.log(modulo.bemVindo)
console.log(modulo)

console.log(modulo2.boaNoite())
console.log(modulo2.bomDia)

funcao = lista => lista.map(n => n * 4)

const lista = [1, 2, 3, 4, 5]

console.log(funcao(lista))



