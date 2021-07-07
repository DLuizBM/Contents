// Object.keys(objeto) -> pega as chaves do objeto

const obj1 = {
    nome: 'João',
    idade: '25'
}
console.log(Object.keys(obj1))

// Object.values(objeto) -> pega os valores do objeto

console.log(Object.values(obj1))

// Object.entries(objeto) -> transforma cada chave valor em uma lista e coloca dentro de uma lista

console.log(Object.entries(obj1))
// [ [ 'nome', 'João' ], [ 'idade', '25' ] ]

Object.entries(obj1).forEach(e => {
    console.log(`${e[0]}: ${e[1]}`)
})

// usando destructuring
Object.entries(obj1).forEach(([chave, valor]) => {
    console.log(`${chave}: ${valor}`)
})


// Object.defineProperty(obj(target), 'chave'(propriedade/atributo){
//      enumerable: true, se ela pode ser listada(aparecer quando for usada funções, como Object.keys())
//      writable: true,  permite ser sobre escrita?
//      value: ?
//})

Object.defineProperty(obj1, 'DatadeNascimento',{
    enumerable: true,
    writable: false,  
    value: '01/01/2019'
})
console.log(obj1.DatadeNascimento)
console.log(Object.keys(obj1))


// Object.assign(dest, ob1, obj2, ...) -> concatena ao objeto dest outro objetos, sobre escrevendo
// variáveis caso exista mais de uma variável igual em um objeto
const dest = {a: 1, b: 2}
const obj = {c: 3}
const obj2 = {d: 4}
const obj3 = {a: 5, e: 6}
const Obj = Object.assign(dest, obj, obj2, obj3)
console.log(Obj)
// { a: 5, b: 2, c: 3, d: 4, e: 6 }, a foi sobre escrito