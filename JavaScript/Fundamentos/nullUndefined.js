let valor // undefined = não foi inicializada
console.log(valor)
valor = null // não está apontando pra nenhum endereço de memória, ausência de valor
// Caso queira zerar o valor de uma variável, atribui-se null
console.log(valor)
 
const produto = {}
produto.preco = undefined // evitar usar undefined, deixar a própria linguagem fazer isso
console.log(produto)
//produto tem um objeto preco com atributo undefined, que é estranho

produto.preco = null // forma correta de 'dizer' que não há atributo
console.log(produto)