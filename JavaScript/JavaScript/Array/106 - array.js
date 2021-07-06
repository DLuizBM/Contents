// O array em js é um tipo especial de objeto

// Formas de criar array
let aprovados = new Array('Ana', 'Bia', 'Carlos')
console.log(aprovados)

aprovados = ['Ana', 'Bia', 'Carlos']
console.log(aprovados)

// Se for chamado um elemento que não está presente no array, ex, aprovados[3]
// será devolvido undefined, em JS não apresenta erro

// Adicionando elementos
aprovados[3] = 'Paulo'
aprovados.push('Abia')
console.log(aprovados.length)

aprovados[9] = 'Rafael'
// os elementos de índice 5, 6 e 7 serão preenchidos com undefined
console.log(aprovados.length)
// saída: 10

// função sort() -> array.sort()
aprovados.sort()
console.log(aprovados)
// ordena pela letra, sendo 'A' a primera e 'Z' a última

delete aprovados[1]
// deletando o elemento de índice 1
console.log(aprovados)

// Função splice 
aprovados = ['Bia', 'Ana', 'Carlos']
aprovados.splice(1, 1)
// a partir do índice 1, desejo excluir 1 elemento, ou seja, vou excluir 'Ana'
//aprovados.splice(1, 2)
// a partir do índice 1, desejo excluir 2 elementos, ou seja, vou excluir 'Ana' e 'Carlos'
console.log(aprovados)
// saída: ['Bia', 'Carlos']

// Excluindo e adicionando elementos
aprovados = ['Bia', 'Ana', 'Carlos']
aprovados.splice(1, 1, 'Elemento1', 'Elemento2')
// a partir do índice 1, desejo excluir 2 elementos, ou seja, vou excluir 'Ana' e 'Carlos'
// e ao mesmo tempo adicionar 'Elemento1' e 'Elemento2'.
console.log(aprovados)

