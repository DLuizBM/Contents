const str = 'Cod3r' // 'JavaScript'
/*
// pegar o caractere

console.log(str.charAt(4))
// pega letra 'S'
console.log(str.charAt(10))
// em caso de índice errado na string, o JS devolve vazio
console.log(str.charCodeAt(4))
// devolve o valor ascii do elemento no índice 3
console.log(str.indexOf('J'))
// devolve o índice do elemento 'J'
console.log(str.substring(1))
// printa a string a partir do índice 1
console.log(str.substring(0, 5))
// printa a string a partir do índice 0 até o indice 5-1 = 4
console.log("Java".concat(' ').concat('Script'))
//console.log("Java" + "Script") no contexto de string o + significa concatenar
// se houvesse '3' + 2 = '32' isso porque  string tem preferência e o + será concatenação
// se houvesse '3' - 2 = 1, pois o - não tem significado na operação com strings, e resultado será a subtração
console.log(str.replace(3, 'e'))
// Substitui o elemento de índice 3 por 'e', só substitui números por letras na string
console.log('Ayrton,Hamilton,Alonso'.split(','))
// Transforma numa lista(array) de string separando por ','
*/   
//////////////////////////////////////////////////////////////////
// TEMPLATE STRING

// ${} --> template string
const nome = 'Ayrton'
const concatenacao = 'Olá' + ' ' + nome

const template = `
    Olá ${nome}
    `
console.log(concatenacao, template)
console.log(`1+1 = ${1+1}`)
// ${1 + 1} fará a soma, pois o $ interpreta como operação matemárica

// Criando função
const up = texto => texto.toUpperCase()
console.log(`Ei...${up('cuidado')}`)

var a1 = 2
var a2 = 4

console.log(`A soma de ${a1} + ${a2} é ${a1+a2}`)

/* exemplo de entrada usando o navegador, só funciona no navegador
for(let i =0; i < 5; i++){ 
    var n2 = parseInt(prompt());
    vet.push(n2+1)
}
*/

