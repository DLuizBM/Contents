// Call e apply são formas de se chamar funções

function getPreco(imposto = 0, moeda = 'R$') {
    return `${moeda} ${this.preco * (1 - this.desc) * (1+ imposto)}`    
}
// this foi usado para pegar o preço e o desconto

const produto = {
    nome: 'Notebook',
    preco: 4589,
    desc: 0.2,
    getPreco // dessa forma ele cria um atributo chamado getPreco e associa a função getPreco

}
console.log(getPreco())
// saída: R$ NaN -> o this.preco e this.desconto no contexto global não está definido
// dessa forma, deve-se colocar valores globais
global.preco = 20
global.desc = 0.1
console.log(getPreco())

console.log(produto.getPreco()) // o Objeto usando o getPreco() como método
// Saída: R$ 3671.2


// CALL

const carro ={preco: 49990, desc: 0.20}
console.log(getPreco.call(carro))

console.log(getPreco.call(carro, 0.17, '$'))
// passando imposto e o símbolo da moeda, diretamente
// carro é contexto que será executado e os parâmetros são passados diretamente 

// APPLY
console.log(getPreco.apply(carro))
console.log(getPreco.apply(carro, [0.17, '$']))
// carro é contexto que será executado e os parâmetros são passados como array 