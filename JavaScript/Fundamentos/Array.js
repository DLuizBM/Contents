const vet = [1, 2, 3.5, true, 'Ayrton']
// Arrays em JS são dinâmicos e suportam qualquer tipo de dado
console.log(vet[0], vet[4])
console.log(vet)
console.log(vet.length)
// Devolve o tamanho do vetor/array

vet.push(4, 5, 'Senna')
// push -> adiciona elementos no array
console.log(vet)
console.log(vet.pop())
// pop() -> retira o último elemento do array e devolve esse elemento
delete vet[1]
// delete tira o elemento especificado pelo índice
console.log(vet)
// Array é do tipo object
