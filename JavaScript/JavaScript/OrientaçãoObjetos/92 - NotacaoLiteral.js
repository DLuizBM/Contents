const a = 1
const b = 2
const c = 3

const obj1 = {a: a, b: b, c: c}
// versão antiga do JS
const obj2 = {a, b , c}
// versão a partir de 2015
// já relaciona a chave 'a' com a constate 'a'...
console.log(obj1)
console.log(obj2)

const nomeAtr = 'Nota'
const valorAtr = 8.9

const obj3 = {}
obj3[nomeAtr] = valorAtr
console.log(obj3)

const obj4 = {[nomeAtr]: valorAtr}
console.log(obj4)


// definindo funções dentro de objeto
// versão antiga
const obj5 = {
    funcao: function(){

    }
}
// versão a partir de 2015
const obj6 = {
    funcao(){
        
    }
}