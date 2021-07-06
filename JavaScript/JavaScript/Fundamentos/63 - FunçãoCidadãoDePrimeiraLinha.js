// Função em JS é firdt-class Object
// High Order function

// Criando de forma literal
function fun1(){}

// É possível armazenar uma função em uma variável
const fun2 = function(){}

// Armazernar função em um array
const array = [function(a, b){}, fun1, fun2]
console.log(array[0](2, 3))
// chamando a função no array

// Armazenar a função dentro de um atributo de um objeto
const obj = {}
obj.fun = function(){return 'falar'}
// Lembrar que o objeto é semelhante o dicionário em pyhton
// logo, fazendo obj.fun, estou colocando dentro do objeto(dicionário)
// a chave fun e o valor dessa chave é function(){return 'fala'}
console.log(obj.fun())

// Passar função como parâmetro
function run(func){
    func() // a chamada da função é feita aqui
}
run(function(){process.stdout.write('Chama a função! \n')})

// Uma função pode retornar/conter uma função
function soma(a, b){
    return function(c){
        console.log(a + b + c)
    }
}
soma(2, 3)(4)
// soma(2,3) retorna uma função, a função retornada precisa de um parâmetro
const Soma = soma(2,3)
Soma(4)
// outra possibilidade

// Parâmetros e retornos são opcionais
