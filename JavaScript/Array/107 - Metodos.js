const pilotos = ['Vettel', 'Alonso', 'Massa']
// pop() -> retira o último elemento do array
pilotos.pop()
console.log(pilotos)
// push() -> adiciona na última posição do array
pilotos.push('Senna')
console.log(pilotos)
// shift -> retira da primeira posição
pilotos.shift()
console.log(pilotos)
// unshift -> coloca na primeira posição
pilotos.unshift('Hamilton')
console.log(pilotos)

// Adicionando com splice
pilotos.splice(2, 0, 'Massa', 'Bottas')
// adicione a partir do índice 2 sem retirar ninguém (0), massa e bottas
// [ 'Hamilton', 'Alonso', 'Massa', 'Bottas', 'Senna' ]
console.log(pilotos)

// Removendo com splice
pilotos.splice(3, 1)
console.log(pilotos)
// [ 'Hamilton', 'Alonso', 'Massa', 'Senna' ]

// Método slice -> retorna um novo array a partir do índice especificado
algunspilotos = pilotos.slice(2)
// a partir do índice 2
console.log(algunspilotos)
algunspilotos = pilotos.slice(1, 4)
// pega os elementos do índice 1 até o índece 4 - 1
// [ 'Alonso', 'Massa', 'Senna' ]
console.log(algunspilotos)