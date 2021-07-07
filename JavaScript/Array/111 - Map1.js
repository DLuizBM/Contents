// Map serve para transformar um array em outro
// não modifica o array atual, transforma em um novo array

const lista = [1, 2, 3, 4, 5]
let a 
let b

a = lista.map(function(num){
    return num * 2
})
console.log(a)

b = lista.map(n => n * 2)

// Maps encadeados

const soma = e => e + 10
const triplo = e => e * 3
const dinheiro = e => `R$ ${parseFloat(e).toFixed(2).replace('.', ',')}`

resultado = lista.map(soma).map(triplo).map(dinheiro)
// lista.map(soma) gera um array, que passa para map(triplo), map(triplo) gera outro array que passa
// para map(dinheiro) e map(dinheiro) gera outro array
console.log(resultado)

// procedimento de map encadeado
let teste = lista.map(soma)
console.log(teste)
let teste2 = teste.map(triplo)
console.log(teste2)
let teste3 = teste2.map(dinheiro)
console.log(teste3)
