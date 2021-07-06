Number.prototype.entre = function(inicio, fim){
    return this >= inicio && this <= fim
}   // this recebe o valor da 'nota' para ser comparado com início e fim

const imprimeNota = function(nota){
    if(nota.entre(9, 10)){
        // nota.entre -> estou passando a nota recebida para o this e ao mesmo tempo 
        // estou passando os argumentos para 'inicio' e 'fim' na função entre
        console.log('Aprovado - SS')
    }else if(nota.entre(7, 8.99)){
        console.log('Aprovado - MS')
    }else{
        console.log('Reprovado')
    }
}
imprimeNota(7)