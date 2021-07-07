// O callback acontece quando é passada uma função é esse função será executada quando um evento ocorrer

const fabricantes = ['Audi', 'BMW', 'Mercedes']

function imprimir(nome, indice){
    console.log(`${indice+1}. ${nome}`)
}
fabricantes.forEach(imprimir)
// for each devolve primeiro o valor(nome) e depois o índice(posição do vetor), por
// 1. Audi
// 2. BMW
// 3. Mercedes

fabricantes.forEach((fabricante, indice) => console.log(fabricante, indice))

// O evento nesse caso é o próprio array que deve ser percorrido
// O callback está presente em linguagens como o python, as funções, map, filter, any, all
// do python, são exemplos de função callback.
// lembrar que para o callback funcionar é necessário o iterável e a função a ser executada
// assim como no python 