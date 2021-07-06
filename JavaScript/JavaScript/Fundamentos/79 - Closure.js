// Closure é o escopo criado quando uma função é declarada
// esse escopo permite a função acessar e manipular variáveis externas a função
// uma função em JS é um closure, por isso a função tem ciência do local em que foi definida
// e acessa aquilo que está mais perto

// contexto lexo em ação

const x = 'Global'

function fora(){
    const x = 'Local'  
    function dentro(){
        return x
    }
    return dentro
}
const funcao = fora()
console.log(funcao())
// Saída: 'Local'
