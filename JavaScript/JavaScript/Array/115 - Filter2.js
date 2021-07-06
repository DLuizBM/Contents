Array.prototype.filter2 = function(callback){
    let array = []
    for(let i = 0; i < this.length; i++){
        if(callback(this[i], i , this) == true){
            array.push(this[i])
        }
    }
    return array
}

const produtos = [
    {nome:'notebook',preco:2499, fragil: true},
    {nome:'ipad',preco: 4199, fragil: true},
    {nome:'copo',preco:12.49, fragil: false},
]

const barato = produto => produto.preco <= 1000 
console.log(produtos.filter2(barato))