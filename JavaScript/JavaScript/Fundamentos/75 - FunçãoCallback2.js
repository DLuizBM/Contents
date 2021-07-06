const notas = [5.6, 7.7, 8, 6.5, 7, 10, 5.5]
var notas_baixas = []
// exemplo sem callback

for(let i in notas){
    if(notas[i] < 7){
        notas_baixas.push(notas[i])
    }
}
console.log(notas_baixas)
notas_baixas = []

// exemplo com callback

notas_baixas = notas.filter(nota => nota < 7)
console.log(notas_baixas)
// usada como no python, onde a função arrow equivale ao lambda
// notas, é o iterável e a função arrow é o que fica sendo chamada recorrentemente