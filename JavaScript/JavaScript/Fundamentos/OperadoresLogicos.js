function comprar(t1, t2){
    comprarTV50 = t1 && t2
    comprarTV32 = t1 != t2
    comprarSorvete = t1 || t2
    saudavel = !comprarSorvete
    // Exemplo : se trabalho1(t1) e trabalho2(t2) forem verdadeiros, então comprartv50
    // também será(operação and), se t1 != t2 (operação xor) então comprartv32 será
    // verdadeira. Se t1 ou t2 verdadeiro, então comprarSorvete é verdadeiro
    // e saudável vai negar comprar sorvete

    return {  comprarTV50, comprarTV32, comprarSorvete, saudavel }
    // está retornando um objeto, já que o return retorna só um valor, então para retornar
    // tudo, retorna-se um objeto com todos os valores. Lembrar que um objeto tem chave
    // valor. Essa forma de retorno é um novo recurso do JS, onde não se precisa especificar
    // o valor, JS já faz isso, porém o valor está implícito, ele existe.

}
console.log(comprar(true, true))
console.log(comprar(true, false))
console.log(comprar(false, true))
console.log(comprar(false, false))