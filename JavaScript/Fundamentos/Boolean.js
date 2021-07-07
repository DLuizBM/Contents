let ativo = false
console.log(ativo)

ativo = true
// let permite que mudemos o valor da vaiável ao longo do programa
console.log(ativo)

ativo = 1
console.log(!!ativo)
// Teste pra saber se é verdadeiro ou falso
// ! -> operador lógico de negação, se !! nega 2 vezes
console.log("Valores verdadeiros")
console.log(!!3)
console.log(!!-1)
console.log(!!' ')
console.log(!![])
console.log(!!{})
console.log(!!Infinity)
console.log(!!(ativo=true))

console.log("Valores falsos")
console.log(!!0)
console.log(!!'')
console.log(!!null)
console.log(!!NaN) //Not a Number
console.log(!!undefined)
console.log(!!(ativo=false))

console.log(!!(''|| 123 || null))
// expressão retorna true, pois nas operações lógicas 123 é true


const nome = ''
console.log(nome || 'Desconhecido')
// Caso nome seja falso, imprima desconhecido
