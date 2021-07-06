Array.prototype.map2 = function(callback){
    let array = []
    for(let i = 0; i < this.length; i++){
        array.push(callback(this[i], i, this))
    }
    return array
}

const carrinho = [
    '{"nome": "borracha", "preco": 3.45}',
    '{"nome": "caderno", "preco": 13.90}',
    '{"nome": "Kit de laps", "preco": 41.22}',
]

const passeJSON = json => JSON.parse(json)
const getPreco = obj => Object.values(obj)[1]
// const getPreco = obj => obj.preco
// do Object.values(obj) estou passando a segunda posição da lista, ou seja, só os valores

let resultado = carrinho.map2(passeJSON).map2(getPreco)
console.log(resultado)