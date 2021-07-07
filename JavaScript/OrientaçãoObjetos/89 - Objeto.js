// Objeto é uma coleção dinâmica de pares chave valor

// criando objetos com atributos dinâmicos (lembrar dos tipos de atributo)
const Pessoa = new Object
Pessoa.nome = 'Senna'
Pessoa['títulos'] = 3
console.log(Pessoa)
delete Pessoa.títulos
console.log(Pessoa)


// criando objetos instanciando a partir da classe
class pessoa {
    constructor(nome){
        this.nome = nome
    }
}
const p1 = new pessoa('Hamiltom')
console.log(p1.nome)


//Criando objetos dentro de objetos

const carro = {
    modelo: 'A4',
    preco: 89000,
    proprietario: {
        nome: 'Raul',
        idade: 56,
        endereco: {
            Rua: 'Rua das Garças'
        }
    },
    condutores: [{ // Array de objetos
        nome: 'Junior',
        idade: 21
    },{
        nome: 'Rafael',
        idade: 24

    }],
    calculaSeguro: function(){

    },
}
// Formas de acesso aos atributos do objeto
console.log(carro.condutores[0])
console.log(carro['condutores'][0])
// Deletando atributos
delete carro.condutores[1]
console.log(carro.condutores)