// classe nada mais é do que uma função, o ideal é usar funções construtoras para trabalhar
// com OO em javascript
// a classe é convertida para função, a classe será transformada numa função construtora

class Lancamento {
    constructor(nome = 'genérico', valor = 0){
        this.nome = nome
        this.valor = valor
    }
}

class CicloFinanceiro {
    constructor(mes, ano){
        this.mes = mes
        this.ano = ano
        this.lancamentos = []
    }
    addLancamento(...lancamentos){
        lancamentos.forEach(l => this.lancamentos.push(l))
    }
    sumario(){
        let valorConsolidado = 0
        this.lancamentos.forEach(l =>{
            console.log(l)
            valorConsolidado += l.valor // l.valor de Lancamento
        })
        return valorConsolidado
    }
}

const salario = new Lancamento('Salario', 45000)
const contaLuz = new Lancamento('Luz', -220)

const contas = new CicloFinanceiro(6, 2018)
contas.addLancamento(salario, contaLuz)
console.log(contas.sumario())

console.log('///////////////////////////////////')

const teste = ['luz', 3000, 200]
teste.forEach(l => console.log(l))