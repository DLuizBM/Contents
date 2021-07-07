for(let i = 0; i < 10; i++){
    console.log('Valor de i: ', i)
}
// console.log('i após o for: ', i)

// Declarando o i com let, o i só estará visível no bloco for

// Problema histórico do JS, mas agora com let
// Com let isso não ocorre, já que let tem escopo de bloco
const fun = []

for (let j = 0; j < 10; j++){
    fun.push(function(){
        console.log(j)
    }
    )
}
fun[0]()
fun[6]()
