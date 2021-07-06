const aprovados = ['Agatha', 'Aldo', 'Daniel', 'Raquel']

aprovados.forEach(function(nome, indice, array){
    // forEache devolve primeiro o valor e depois o índice
    // é possível também a cada execução do forEach, buscar o array que está sendo trabalhado
    console.log(`${nome}, ${indice}`)
    console.log(array)
})

aprovados.forEach(nome => console.log(nome))
// valor é sempre passado primeiro, caso queria acessar o índice, deve-se passar os 2 e pegar
// só o índice

const exibirAprovado = aprovado => console.log(aprovado)
aprovados.forEach(exibirAprovado)
// forEache vai pegar cada elemento de 'aprovados' e mandar para exibirAprovado imprimir