console.log(Math.ceil(6.1))
// Math.ceil, faz o arredondamento pra cima, 6.1 para 7

const obj = {}
obj.nome = 'Ayrton'
// Essa é a notação ponto
//obj['nome'] = 'Senna' // outra forma de adicionar uma chave/valor no obj, mas dá-se 
// preferência para a notação ponto
console.log(obj.nome)

function Obj(Name){
    this.nome = Name
    this.exec = function(){
        console.log('Entendeu?')
    }
}
// Recebe o parâmetro Name (linha 11), que vai para a variável Name (linha 12)
// this.nome -> this especifica o obj que está com a variável Name e a chamada é feito pelo .nome
// ex - quando criado o obj2, o this.nome é como se fosse o obj2 apontando para o seu 'Name'
// já o obj3 quando criado, passa o 'Alô' para Name e seu Name é 'Alô', o this.nome
// do obj3 aponta para o 'Name' 'Alô' 
// A função vai ficar pública para ser usada por vários objetos


const obj2 = new Obj('Olá')
console.log(obj2.nome)

const obj3 = new Obj('Alô')
console.log(obj3.nome)
obj3.exec()
// como obj3 foi criado como new Obj, é possível usar os recursos de Obj
// logo é possível chama o this.exec

