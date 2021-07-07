// This -> referencia o objeto atual daquela execução

const pessoa = {
    saudacao: 'Bom dia!',
    falar(){    // apesar do objeto ter chave valor, criar uma função num objeto é um recurso novo
            console.log(this.saudacao)
                // this.saudacao -> é a saudação do objeto no qual é o dono dessa função
                // acessando o atributo desse abjeto
    }
}
pessoa.falar() // acessando a função falar do objeto pessoa, this aponta para o objeto pessoa

const fala = pessoa.falar
// armazenando a função falar dentro da variável fala. Para armazenar a função/atributo de um objeto
// em uma variável, deve-se fazer variavel = obj.atributo
fala()
// como a variável fala recebeu a função falar, para trabalhar com essa variável, deve-se usar (), já
// que essa variável 'se tornou' a função, e chamada de função é com ()
// saída de fala() é undefined - pois dessa forma, saudação está apontando para um this que não
// é mais do objeto pessoa.

// Resolver com a função bind(objeto)

const falando = pessoa.falar.bind(pessoa)
falando()
// o bind aponta sempre para o this do objeto, logo  a variável falando vai receber a função
// falar do objeto pessoa, apontando sempre para aquele objeto(bind(pessoa))

////////////////////////////////////////////////////////////////////////////////
/*
function Pessoa(){
    this.idade = 0
    setInterval(function(){
        this.idade++
        console.log(this.idade)
    } ,1000)// setInterval -> dispara outra função a partir de um determinado intervalo
            // vai disparar a function a cada 1000ms =  1s
            // possível colocar funções como parâmetros de outras funções
}
new Pessoa
// instanciando a partir da função pessoa para criar um objeto
// somente fazendo a chamada para criar o objeto
// Este exemplos serve para mostrar que o this pode variar (assim como no brows) e ele vai variar de acordo
// com quem está chamando essa função, no exemplo acima quem está disparando a chamada da função
// é o temporizador da setInterval e não o objeto pessoa, dessa forma o this não aponta para
// o objeto pessoa. A saída será NaN
*/
function Pessoa(){
    this.idade = 0
    //const self = this
    setInterval(function(){
        this.idade++
      //self.idade++
        console.log(this.idade /*self.idade*/)
    }.bind(this) /* self*/,1000)
    // notação ponto .bind(this), colocando a função bind com this, ele vai amarrar
    // o this do objeto a chamada da função, dessa forma, apontando de fato para pessoa
    // o self também pode ser usado, pois é amarrado a ele o this que está na função Pessoa
    // indicando que o this que eu quero apontar é o da função Pessoa
}
new Pessoa