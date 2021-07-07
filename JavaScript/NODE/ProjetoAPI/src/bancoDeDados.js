const sequence = {
    _id: 1,
    get id(){
        return this._id++
    }
}

const produtos = {}

function salvarProduto(produto){
    if(!produto.id){
        produto.id = sequence.id
        // sequence.id está executando a função id(). Por conta do get não é necessário sequence.id()
        // dessa forma, está incrementando no _id. Na primeira iteração o valor é o setado no _id
    }
    produtos[produto.id] = produto
    return produto

}

function getProduto(id){
    return produtos[id] || {}
}

function getProdutos(){
    return Object.values(produtos)
    // retornando apenas os valores do objeto
}

function deletarProduto(id){
    const produto = produtos[id]
    delete produtos[id]
    return produto
}

// tornando as funções visíveis para todo o módulo
module.exports = {salvarProduto, getProduto, getProdutos, deletarProduto}
