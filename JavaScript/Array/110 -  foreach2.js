Array.prototype.forEach2 = function(callback){
    // o parâmetro callback é uma função que deve ser passada
    for(let i = 0; i < this.length; i++){
        // o acesso ao array dentro de uma função que pertence ao prototype é feito pelo this
        // acessando a instância de um array pelo this
        callback(this[i], i, this)
    }
}

const lista = [10, 20, 30]

lista.forEach2(function(nome, indice){
    console.log(nome, indice)
})