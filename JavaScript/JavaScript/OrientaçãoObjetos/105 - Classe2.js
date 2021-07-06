class Avo {
    constructor(sobrenome){
        this.sobrenome = sobrenome
    }
}

class Pai extends Avo {
    constructor(sobrenome, profissao = 'Professor'){
        super(sobrenome)
        this.profissao = profissao
    }
}

class Filho extends Pai {
    constructor(){
        super('Silva')
        // com o construtor vazio, estou herdando o constutor do pai
        // super('Silva), definindo apenas o sobrenome, a profissão vai herdar o valor padrão
        // Professor
    }
}

const filho = new Filho()
console.log(filho)