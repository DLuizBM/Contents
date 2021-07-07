/* Função Arrow
- Criada para ter uma sintaxe reduzida e ter um this associado ao contexto 
- no qual a função foi escrita

let dobro = function(a){
    return a * 2
}
// Exemplos de função arrow
dobro = (a) => {
    return a * 2
}
dobro = a =>  a * 2 // pode ser escrita dessa forma quando se tem apenas 1 parâmetro
                    // e sem chaves, o retorno fica implícito

let ola = function(){
    return 'olá'
}
ola = () => 'olá'
ola = _ => 'olá' // _ é um parâmetro, mas como não está sendo usado, nem tem problema


// o uso de arrow function garante que o this não varia ao longo da execução da função

function pessoa(){
    this.idade = 0
    setInterval(()=>{ 
        this.idade++
        console.log(this.idade)
    }, 1000)
}
new pessoa

*/


var compara = function(param){
    console.log(this == param)
}
compara(global)
// global é um objeto do node, semelhante ao window no browser
// this aqui é o global
const obj = 0
abc = compara.bind(obj)
abc(global)
abc(obj)
// amarrando a variável obj a chamada de compara com o bind, a variável obj será o this pra chamada dessa função
// desse forma, sempre que abc for chamado o this vai apontar para obj e não para o escopo global

let comparaArrow = param => console.log(this == param)
comparaArrow(global)
// Com a função Arrow, o this não aponta para o global como uma função normal apontaria
// o this numa função arrow é um this associado ao contexto no qual a função foi escrita
// mesmo forçando a variação de contexto com o bind, isso não é possível

