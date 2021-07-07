// Como declarar números
const peso = 2.0
const kg = Number('1') // Number - converte string em tipo numérico

console.log(peso, kg)
console.log(Number.isInteger(peso))
// Método que verifica se um número é inteiro, retorna True ou False
// Em JS se o número é colocado 4.0, o fato de ter colocado .0 não faz com seja ponto flutuante

const total = peso * 2.42999 + kg * 1.599
console.log(total.toFixed(2)) // Método para fixar casas decimais
console.log(total.toString(2)) // Com o 2 dentro transforma em binário, sem o 2 pra string
console.log(typeof total)

////////////////////////////////////
// Operações interessantes
console.log(7/0) // tipo infinity
console.log("10"/2) // "10,2" não funciona "10.2" funciona
console.log("Show"*2) // Em algumas linguagens funciona, JS não
//console.log(10.toString()) Não funciona
console.log((10).toString) // Funciona

// Uso do math

const raio = 5.6
const area =  Math.PI * Math.pow(raio, 2)
console.log(area)


