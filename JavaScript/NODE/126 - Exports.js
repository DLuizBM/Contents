console.log(module.exports == this)
console.log(module.exports == exports)

this.a = 1
exports.b = 2
module.exports.c = 3
console.log(module.exports)

// this, exports e module.exports são a mesma coisa
// porém quem é retornado é o module.exports, ou seja, this e exports se tornam module.exports