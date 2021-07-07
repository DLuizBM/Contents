// uma função pode não receber parâmetros, mas é possível recuperar esses parâmetros
// no decorrer da função, com 'arguments' que busca parâmetros a partir da chamada
// de uma função, ele é um array

function soma(){
    let soma = 0
    for (i in arguments){
        soma += arguments[i]
    }
    return soma
}
console.log(soma())
// cuidado ao usar process.stdout.write()
// não chamou a função
console.log(soma(1, 2, 3, 4, 5))
console.log(soma(1, 2, 3, ' teste'))