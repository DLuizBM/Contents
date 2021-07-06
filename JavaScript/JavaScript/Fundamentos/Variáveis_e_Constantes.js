var a = 3
let b = 4
// É possível criar variáveis com var ou let
// Existem diferenças entre var e let, let é uma forma mais moderna de criar variável
// var permite que uma variável seja redeclarada dentro de um mesmo escopo, let não permite

var a = 30
console.log(a, b)

a = 300
b = 400
console.log(a, b)

const c = 5
// Tudo que não precisa ser mudado dentro de um programa deve ser usado como constante
// Não é possível reatribuir valores a constantes
// c = 500, seria apresentado erro

console.log(c)
