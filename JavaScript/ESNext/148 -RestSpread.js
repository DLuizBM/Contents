// Esse operador pode ser usado para juntar(rest) e para espalhar(spread)

// usando com objetos

const funcionario = {nome: 'Maria', salario: 12000.00}
const clone = {ativo: true, ...funcionario}
// colocando funcionário dentro de clone
console.log(clone)

function soma(...lista){
    // agrupando em um array [1, 2, 3, 4] para ser usado pela função reduce
    console.log(...lista)
    // spread usado mais uma vez saída: 1, 2, 3, 4
    const list = lista.reduce((x, y) => x + y)
    console.log(list)
}
const array = [1, 2, 3, 4]
console.log(...array)
soma(...array)
// espalhando em 1, 2, 3, 4. Ou seja, tirando de um array
