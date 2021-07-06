// Object.preventExtensions -> não permite que novos atributos sejam incluídos no objeto
// permite que sejam excluídos e que sejam modificados
const produto = Object.preventExtensions({
    nome: 'Qualque', preco: 1.99, tag: 'promoção'
})

console.log('Extensível: ', Object.isExtensible(produto))
produto.nome = 'borracha'
produto.quantidade = 7
// nada vai acontecer, já que esse atributo não existe e nem será criado
delete produto.tag
console.log(produto)

// Object.seal -> não permite adicionar atributo e nem excluir, mas permite modificar os valores
const pessoa = {nome: 'Maria', idade: '63'}
Object.seal(pessoa)
pessoa.nome = 'José'
pessoa.cabelo = 'Branco'
delete pessoa.idade
console.log('Selado: ', Object.isSealed(pessoa))
console.log(pessoa) 