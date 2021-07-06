// notação litera
const obj1 = {}

// Object em JS
const obj2 = new Object

// Funções construtoras

function Produto(nome, preco, desconto){
    this.nome = nome
    this.getPrecoDesconto = () => {
        return preco  * (1 - desconto)
    }
}
const p1 = new Produto('caneta', 1.99, 0.15)
const p2 = new Produto('notebook', 4999, 0.20)
console.log(p1.getPrecoDesconto(), p2.getPrecoDesconto()) 

// Função Factory
function criarFuncionario(nome, salario, faltas){
    return {
        nome,
        salario, 
        faltas,
        getSalario(){
            return (salario/30) * (30 - faltas)
        }
    }
}
const f1 = criarFuncionario('João', 9000, 2)
console.log(f1.getSalario())
console.log(f1.nome)

// Object.create
const filha = Object.create(null)
filha.nome = 'Ana'
console.log(filha)

// Uma função que retorna objeto
const fromJSON = JSON.parse('{"info":"Sou um JSON"}')
console.log(fromJSON.info)
