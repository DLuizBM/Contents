const ferrari = {
    modelo: 'f40',
    velMax: 324,
}

const volvo = {
    modelo: 'v40',
    velMax: 200,
}

// obj.__proto__: acessa ao protótipo do objeto, ou seja, o super objeto, o objeto pai
// se tentar achar um atributo dentro de ferrari e não encontrar dentro de ferrari ele busca no objeto pai
// se não achar, procura em toda a cadeia de protótipos e se achar, ele retorna, se não retorna undefined 

console.log(ferrari.__proto__)
// saída: {}, o protótipo de ferrari é um objeto vazio
console.log(ferrari.__proto__ === Object.prototype)
// um objeto criado por padrão aponta para Object.prototype
// Object.prototype representa o prototype de mais alto nível, depois dele não há mais nada
console.log(volvo.__proto__ === Object.prototype)
console.log(Object.prototype.__proto__)
// Será que Object.prototype tem um protótipo de mais alto nível depois dele?
// Saída: null, a resposta é não

// Object é uma função com atributo prototype

function MeuObjeto() {}

console.log(typeof MeuObjeto)
console.log(MeuObjeto.prototype)
// saída: MeuObjeto {}
console.log(Object.prototype)

