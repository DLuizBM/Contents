// Criando objetos com o create, create já referência o protótipo
const pai = {nome: 'Pedro', cabelo: 'preto'}

const filha1 = Object.create(pai)
filha1.nome  = 'Ana'
filha1.idade = 23
console.log(filha1.nome)
console.log(filha1.cabelo)

const filha2 = Object.create(pai, {
    nome: {value: 'Bia', writable: false, enumerable: true}
})
console.log(`${filha2.nome} tem cabelo ${filha2.cabelo}`)


for(let key in filha1){
    console.log(key)
}

console.log('\nhasOwnProperty \n')

for(let key in filha1){
    filha1.hasOwnProperty(key) ? console.log(key) : console.log(`Por herança ${key}`)
    // se a propriedade é do objeto, imprima a chave, se não imprima 'Por herança key'
}