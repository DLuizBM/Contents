// sem promise

const http = require('http')

const getTurma = (letra, callback) => {
    url = `http://files.cod3r.com.br/curso-js/turma${letra}.json`
    http.get(url, res => {
        let resultado = ''

        res.on('data', dados => {
            resultado += dados
        })

        res.on('end', () => {
            callback(JSON.parse(resultado))
        })
    })
} 


// Callbacks Aninhadas 

getTurma('A', alunos => {
    nomes = alunos.map(aluno => `A: ${aluno.nome}`)
    console.log(nomes)

    getTurma('B', alunos => {
    nomes = alunos.map(aluno => `B: ${aluno.nome}`)
    console.log(nomes)
    })

    getTurma('C', alunos => {
    nomes = alunos.map(aluno => `C: ${aluno.nome}`)
    console.log(nomes)
})
})


// Não é possível utilizar os valores passados para o array fora da função
// console.log(nomes) -> será vazio


/*
Essa forma precisa da declaração de um array fora da função
Não é possível utilizar os valores passados para o array
Fora da função

let nomes = []
getTurma('A', alunos =>{
    nomes = nomes.concat(alunos.map(a => `A: ${a.nome}`))
    console.log(nomes)
})
console.log(nomes + 'Array vazio :(')
// array vazio
*/
