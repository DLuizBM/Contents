const alunos = [
    {nome:'João', nota:7.2, bolsista: false},
    {nome:'Maria', nota:9.2 , bolsista: true},
    {nome:'Pedro', nota:9.8, bolsista: false},
    {nome:'Ana', nota:9.8, bolsista: false},
]

const resultado = alunos.map(a => a.nota).reduce(function(acumulador, atual){
    console.log(acumulador, atual)
    return acumulador + atual
    // return é necessário para estar sempre atualizando o acumulador
}, 0)
// 0 é o valor inicial,
console.log(resultado)
// saída: 36

const teste = alunos.map(a => a.nota).reduce((acumulador, atual) => acumulador + atual, 10) // 10 é o valor inicial 
console.log(teste)
// saída: 36 sem o 10 de valor inicial
// saída: 46 com o 10 de valor inicial