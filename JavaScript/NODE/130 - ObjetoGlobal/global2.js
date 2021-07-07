// forma de se chamar o objeto global
require('./global')
console.log(Minhaapp.saudacao())
console.log(Minhaapp.nome)

// Minhaapp está vindo do objeto global e não do arquivo global.js

console.log(this == global)
// Falso: this não aponta para global e sim module.exports

// Dentro de uma função this não aponta para module.exports

function logThis(){
    console.log("This não aponta para module.exports aqui dentro!")
    console.log(this === module.exports)

    // dentro de função, this aponta para global
    console.log(this === global)

    this.perigo = '...'
    // como this aponta para o global dentro de uma função
    // ao fazer isso, perigo está no objeto global agora
    // CUIDADO

    
}
this.perigo = '...'
// Aqui está dentro do module.exports

logThis()