const escola = [{
    nome: 'turma M1',
    alunos: [{
        nome: 'Gustavo',
        nota: 8.1
    }, {
        nome: 'Ana',
        nota: 9.3
    }]
},{
    nome: 'turma M2',
    alunos:[{
        nome: 'Rebeca',
        nota: 8.9
    }, {
        nome: 'Roberto',
        nota: 7.3
    }]
}]


const getNota = aluno => aluno.map(dic => dic.nota)
let notas = escola.map(aluno => aluno.alunos).map(getNota)
console.log(notas)


const getNotas = aluno => aluno.nota 
const getNotasTurma = turma => turma.alunos.map(getNotas)
let Notas = escola.map(getNotasTurma)
console.log(Notas)

Array.prototype.flatMap = function(callback){
    return Array.prototype.concat.apply([], this.map(callback))
}
const notas1 = escola.flatMap(getNotasTurma)
console.log(notas1)