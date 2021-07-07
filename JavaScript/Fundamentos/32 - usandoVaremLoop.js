for(var i = 0; i<10; i++){
    console.log("Valor de i: ", i)
}

console.log('Valor de i após o loop: ', i)
// Mesmo em um laço, a variável i, declarada com var, ficou visível para todo o programa

// Problema histórico do JS
// loop que adiciona função em um vet, cada funcão deve imprimir o valor de i que 
// está no loop. 
const fun = []

for (var i = 0; i < 10; i++){
    fun.push(function(){
        console.log(i)
    }
    )
}
fun[0]()
fun[6]()
// O valor impresso será o mesmo para cada função dentro do array, pois como i foi declado
// com var, a variável se torna global, nesse caso, mesmo que no escopo da função(uma excessão),
// mas lembra que var tem escopo de função.





