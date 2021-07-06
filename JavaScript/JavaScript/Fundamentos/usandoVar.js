{
    {
        {
            {
                var valor = 10
             }
        }
    }
}

console.log(valor) // Visível, mesmo fora do bloco de código

// Em JS se for usado var pra declarar variável, ela ficará visível em todo o código
// mesmo que esteja em um bloco de código, como acima. Ela só não será visível se 
// estiver em uma função, como mostrado abaixo

function mostra(){
    var nome = 'VAI MOSTRAR??'
}
mostra()
// console.log(nome)  Erro, pois nome não é visível fora da função

// Em JS é possível ter 2 ou mais variáveis iguais, desde que em escopos diferentes
// variáveis globais sobreescrevem locais, por isso, deve-se evitar variáveis globais
// Não existe escopo de bloco para uma variável tipo var, somente dentro de função, se
// tiver função, considera-se o bloco maior, logo, no programa abaixa é considerado
// o valor 2 para a variável número, pois ela foi declarada uma segunda vez com esse valor


var numero = 7

{
    var numero = 2
    console.log('dentro = ', numero)
}

console.log('fora = ', numero)