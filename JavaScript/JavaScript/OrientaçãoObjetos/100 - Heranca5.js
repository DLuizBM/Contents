console.log(typeof String)
console.log(typeof Array)
console.log(typeof Object)
// Saída: function -> toda função tem um atributo chamado .prototype

// inserindo um método reverse no protótipo de String
String.prototype.reverse = function(){
    return this.split('').reverse().join('')
}
console.log('Escola'.reverse())

// criando uma método para pegar o primeiro elemento de array
Array.prototype.first = function(){
    return this[0]
}
// para acessar a string, array, etc. Usa-se a this
console.log([1, 2, 3].first())

// tomar cuidado ao criar e substituir funções já existentes 
String.prototype.toString = function(){
    return 'Lascou tudo'
}
// toString já existe no protótipo, estamos substituindo seu comportamento original