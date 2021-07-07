/*
1 - De atribuição
a = 10
b = 5
b += a
b -= 4
b *= 2
b /= 2
console.log(b)
b %= 2 // resto igual
console.log(b)

2 - Destructuring
Serve para tirar atributos de dentro de um objeto


const piloto = {
    nome: 'Lewis',
    sobrenome: 'Hamilton',
    equipes: {
        mclaren: '2007 - 2012',
        mercedes: '2013 - '
    }

}

// Retirando alguns atributos do objeto piloto
const {nome, equipes} = piloto
// retire para mim, os atributos nome e equipes do objeto piloto
console.log(nome, equipes)
const {nome: i, sobrenome: j} = piloto
// retire para mim, os atributos nome e sobrenome do objeto piloto e coloque na variável i e j
console.log(i, j)
const{equipes:{mclaren, mercedes}} = piloto
// Acessando os atributos mclaren e mercedes
console.log(mclaren, mercedes)

// Se algum atributo não estiver dentro do objeto o JS vai setar com undefined


// Destruturing em arrays

const a = [1, 2, 4, 5, 6, 7, 7, 8, 9]
const [n1, n2, n3] = a
console.log(n1, n2, n3)
const [n11, , n33, , n55] = a
console.log(n11, n33, n55)

// pode-se ignorar elementos dentro do array e buscar só os interessados
// na linha 45, só os 3 primeiros elementos foram selecionados
// na linha 47 os elementos 1, 3 e 5, o restante foi ignorado

const b = [1, [2, 3]]
const [ , [a1, ]] = b
console.log(a1)  // saída = 2
// ignorando o primeiro elemento do vetor, pegando segungo elemento, mas dentro do segundo
// selecionando o que está na primeira posição, no caso, a1


function rand({min = 0, max = 1000 } = {}){
    // caso não seja passado um objeto, terá o valor padrão {}
    // usando o destruturing para pegar o max e o min
    valor = max - min
    return Math.floor(valor)
}
console.log(rand({min : 40, max : 50}))
// chamando a função e passando um objeto para ela
const obj = {max:30, min:10}
console.log(rand(obj))
// outra forma de fazer

*/

function rand({min = 0, max = 1000}){
    if (min>max)[min, max] = [max, min]
    valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}

console.log(rand([50, 40]))
console.log(rand({min: 10, max: 20}))
// a função tem 2 valores default
// poderia passar apenas 1 ou nenhum dos 2 valores que daria certo
console.log(rand([]))
// console.log(rand()), errado, pois tentará desestruturar elementos de algo nulo

/////////////////////////////////////////////////////////////////////////////////

// Operadores unários

let num = 1
let num2 = 2

num++ // forma pós fixada
console.log(num)
--num // forma pré fixada
console.log(num)

console.log(++num === num2--)
// essa expressão é true, pois o ++num1 é executado antes da comparação
const  A = 2
const  B = 3
console.log(A === B)
// === compara o valor e o tipo, para ser true os 2 devem ser verdadeiros
