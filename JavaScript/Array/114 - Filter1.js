const produtos = [
    {nome:'notebook',preco:2499, fragil: true},
    {nome:'ipad',preco: 4199, fragil: true},
    {nome:'copo',preco:12.49, fragil: false},
]

// em comparação map e forEach devolvem falso
produtos.forEach(function(produto){
    console.log(produto.preco > 200)
})
// saída: 
// true
// true
// false
console.log(produtos.map(produto => produto.preco > 200))
// saída: [ true, true, false ]

// Map e filter devolvem array, já forEach devolve cada elemento

console.log(produtos.filter(function(produto){
    return produto.preco > 200
}))

// Filter encadeado
const barato = produto => produto.preco <= 1000
const fragilidade = frg => frg.fragil == false
console.log(produtos.filter(barato).filter(fragilidade))