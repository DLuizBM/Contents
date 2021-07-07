// Função anônimas é uma função sem nome

var soma = function(x, y){
    return x + y
}
console.log(soma(3, 4))

const imprimirResultado = function (a, b, operacao = soma){
    console.log(operacao(a, b))

}
imprimirResultado(3, 4)
imprimirResultado(3, 4, soma)
imprimirResultado(3, 4, function(x, y){
    return x - y 
})
// o parâmentro operação recebe como argumento a function(x, y). a e b serão passados
// como argumentos para os parâmetro x e y
imprimirResultado(3, 4, (x,y) => x * y)
// funções arrow sempre são anônimas
const pessoa = {
    falar: function(){
        console.log('Olá!!')
    }
}
pessoa.falar()
// acessando a função anônima a partir de um atributo do objeto que foi definido