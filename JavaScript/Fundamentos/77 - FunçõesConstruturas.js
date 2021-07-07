// A função construtura em JS é semelhante a classe em JAVA
// a partir de uma classe é possível criar instâncias
// em JS é possível criar funções e instanciar funções

function carro(velMax = 200, delta = 5){
// como se estivesse criando um constrututor de um objeto e passando dados para esse construtor

    // atributo privado(pertence apenas ao escopo dessa função(função carro))
    // quando for instanciar o objeto a partir dessa função, não há como acessar diretamente objeto.velocidadeAtual
    // porque esse é uma atributo interno da função
    let velocidadeAtual = 0

    // criando um método público (palavra reservada this)
    this.acelerar = function (){
        if(velocidadeAtual + delta <= velMax){
            velocidadeAtual += delta
        }else{
            velocidadeAtual = velMax
        }
    }

    // criando outro método público
    this.getvelocidadeAtual = function(){
        return velocidadeAtual
    }
    
}

// instanciando um objeto

const uno = new carro
uno.acelerar()
// chamando acelerar que é um método público
console.log(uno.getvelocidadeAtual())
// chamando getvelocidadeAtual do método público

const ferrari = new carro(350, 20)
ferrari.acelerar()
console.log(ferrari.getvelocidadeAtual())

// notar as 2 instâncias diferentes a partir da mesma função construtora