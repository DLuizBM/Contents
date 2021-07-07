// this no JS é o self no Python

// Exemplo 1
class Pessoa{
    constructor(nome, telefone){
        this.nome = nome
        this.telefone = telefone
    }
    
    campeao(){ // criando o método campeão (this.nome JS == self.nome em Python)
        console.log(`O campeão mundial é ${this.nome}`)
    }
}
const p1 = new Pessoa('Senna', '555-5555')
// usar a palavra reservada new para instanciar um objeto a partir da classe
console.log(p1.nome)
console.log(p1.telefone)

// Chamando o método campeao
p1.campeao()

// Exemplo 2

const CriarPessoa = nome =>{
    return {
        falar: () => console.log(`Meu nome é ${nome}`)
    }
}
const p2 = CriarPessoa('Hamilton')
p2.falar()

// Exemplo 3 - Passando o exemplo 1 para função construtora

function Pessoas(nome) {
    this.nome = nome

    this.falar = function () {
        console.log(`Meu nome é ${this.nome}`)        
    }
}

const p3 = new Pessoas('Ayrton Senna')
console.log(p3.nome)
p3.falar()