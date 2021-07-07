Array.prototype.reduce2 = function(callback, valorInicial){
    const indice = valorInicial ? 0 : 1
    // se houver valor inicial, então 'indice' é 0, se não 'indice' é 1
    let acumulador = valorInicial || this[0]
    // colocando a condição para ter valor inicial
    for(let i = indice; i < this.length; i++){
        acumulador = callback(acumulador, this[i])
    }
    return acumulador
}
const alunos = [
    {nome:'João', nota:7.2, bolsista: false},
    {nome:'Maria', nota:9.2 , bolsista: true},
    {nome:'Pedro', nota:9.8, bolsista: false},
    {nome:'Ana', nota:9.8, bolsista: false},
]

total = (acumulador, nota) => acumulador + nota
let somanotas = alunos.map(dic => dic.nota).reduce2(total, 5)
console.log(somanotas)