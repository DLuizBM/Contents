let numero = 7
{
    let numero = 2
    console.log('dentro = ', numero)
}

console.log('fora = ', numero)

// Diferentemente de var, a variável let somente fica visível no bloco em que está declarada
// Var -> escopo global e de função
// Let -> escopo global, de bloco e de função

let numero3 = 7
{
    let numero2 = 2 
    // Nesse caso as duas saídas serão 7, pois ao mandar imprimir a variável numero
    // ele vai procurar no escopo interno (dá preferência para o escopo interno) se essa variável existe, caso não, ele vai procurar
    // em um escopo mais externo. 
    console.log('dentro = ', numero3)
}

console.log('fora = ', numero3)