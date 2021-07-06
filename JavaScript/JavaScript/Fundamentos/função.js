// Função sem retorno
function imprimaSoma(a, b){
    console.log(a + b)
}
imprimaSoma(1, 2)
imprimaSoma(2) // retorna um Not A Number
// Se não for passado um número menor de parâmetros, o parâmetro sem valor será undefined
// será retornado o NaN (not a number), se for passado mais parâmetros, será pegado
// o número correto de parâmetros e o resto será ignorado
imprimaSoma(2, 3, 4, 5,6)

// Função com retorno e parâmetro padrão se o argumento não for passado
function subtracao(a, b = 0){
    return a - b
}
console.log(subtracao(2, 1))
console.log(subtracao(10))

// Armazenando uma função em uma variável

const soma = function(a, b){
    console.log(a + b)
}

soma(10, 20)

// Armazenando uma função arrow em uma variável
const multiplicacao = (a, b) => { // => substitui o 'function'
    return a * b
}
console.log(multiplicacao(2, 3))

// Retorno implícito
const div = (a, b) => a / b
// função retorna o valor do cálculo sem precisar do return
console.log(div(10, 5))
const legal = a => console.log(a)
legal('Legal!!')