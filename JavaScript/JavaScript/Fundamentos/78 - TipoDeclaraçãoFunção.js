console.log(soma(3, 4))
// function declaration || a chamada da função pode ser feita antes de sua declaração
// pois o JS carrega todos as funções primeiro para poder depois usá-las, só funciona com function declaration
function soma(x, y){
    return x + y
}

// function expression || não pode ser chamada antes de sua declaração
const sub = function(x, y){
    return x - y
}
console.log(sub(3, 4))

// named function expression || não pode ser chamada antes de sua declaração
const mult = function mult(x, y){
    return x * y
}
console.log(mult(3, 4))