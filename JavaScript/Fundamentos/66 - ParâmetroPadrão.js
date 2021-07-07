// gerando parâmetro padrão, método 1
function soma(a, b, c){
    a = a || 1 // se a possuir algum valor, recebe esse valor, se a não possuir nenhum valor recebe 1
    b = b || 1
    c = c || 1
    return(a + b + c)
}
console.log(soma(), soma(1, 2, 3), soma(0, 0, 0))
// o problema é quando são passados valores nulos(0, 0, 0), pois como o é false, os valores
// na função vão receber 1, e a soma será 3

// método 2, 3 e 4

function soma2(a, b, c){
    a = a !== undefined ? a : 1 // a diferente de undefined ? se sim recebe a, se não : recebe 1
    b = 1 in arguments ? b: 1 // o parâmetros na função são organizados por índice, logo no índice 0 está 
                              // a, no índice 1 está b e no índice 2 está c. Dessa forma,
                              // b = 1 in arguments ? -> existe algum argumento do índice 1, se sim b recebe b : se não recebe 1
    c = isNaN(c) ? 1: c       // A variável c is not a number ? caso seja, retore o valor padrão, caso não, retorne o valor c
    // mais seguro
    return a + b + c 
}
console.log(soma2(1, 2, 3), soma2(0,0,0))

// método 5, método mais usado, versão mais nova
function soma3(a = 1, b = 1, c = 1){
    return a + b + c
}
console.log(soma3(0,0,0), soma3(1, 2, 3))


