function MeuObjeto(){}
console.log(MeuObjeto.prototype)
// o atributo prototype aponta para MeuObjeto{}


const obj1 = new MeuObjeto
const obj2 = new MeuObjeto

console.log(obj1.__proto__)
// saída: MeuObjeto{}
console.log(MeuObjeto.prototype === obj1.__proto__)

// Toda função tem o atributo prototype. __proto__, como um objeto referência o seu protótipo
// quando se cria um objeto de forma literal, o protótipo dele é Object    

MeuObjeto.prototype.nome = 'Anônimo'
MeuObjeto.prototype.falar = function(){
    console.log(`Bom dia!! Meu nome é ${this.nome}`)
}
obj1.falar()
obj2.nome = 'Rafa'
obj2.falar()

obj3 = {}
// dessa forma a referência do objeto é Object.prototype
console.log(obj3.__proto__)
// saída: {}


obj3.__proto__ = MeuObjeto.prototype
// mudando a referência de Object.prototype para MeuObjeto.prototype
console.log(obj3.__proto__)

// Resumo
console.log((new Object).__proto__ === MeuObjeto.prototype)
console.log(MeuObjeto.__proto__ === Function.prototype)
// __proto__ é um atributo, a função também tem um atributo __proto__
console.log(Function.prototype.__proto__ == Object.prototype)
// o protótipo do protótipo de uma função, aponta para Object.prototype
console.log(Object.prototype.__proto__ === null)

