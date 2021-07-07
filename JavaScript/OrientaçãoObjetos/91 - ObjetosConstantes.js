// Por que é possível manipular objetos definidos como const, como exemplo a seguir?
const pessoa = {nome: 'João'}
console.log(pessoa.nome)
pessoa.nome = 'Pedro'
console.log(pessoa.nome)
// quando se define uma constante, essa constante vai apontar para um endereço de memória e no endereço 
// vai estar contido o objeto. Quando se muda o valor de João para Pedro não se muda o endereço
// aonde o objeto está, ou seja, pessoa continua apontando para o mesmo endereço. Muda-se o valor do objeto.

Object.freeze(pessoa)
// congela o objeto, não sendo possível alterar, deletar ou inserir novos atributos.
pessoa.nome = 'Maria' // ignorado quando se tem o freeze
console.log(pessoa.nome)