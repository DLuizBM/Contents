// Hoisting -> içamento
// Todo programa é lido de forma sequencial, dessa maneiro se quisermos usar uma variável
// na linha 2, é necessário tê-la declarado na linha 1, em JS por conta do 'var'
// isso não acontece, por ser que uma variável declarada apenas na linha 10 seja usada
// na linha 3, quando isso acontece o JS iça(hoisting) a variável para que seja usada
// na linha 3. O código não apresenta problema, mas se usada antes de declarada
// o valor será undefined
// NÃO EXISTE MOTIVO PARA USAR ESSE RECURSO, SEMPRE DECLARAR AS VARIÁVEIS ANTES DO USO
// Dentro de função a mesma coisa acontece

console.log('Variável será declara apenas na linha 10, que é 1000: ', numero)
// Saída: undefined
var numero = 1000
console.log('Agora fui declarada: ', numero)

//
