// While
// Mais indicado quando não se sabe ao certo o número de vezes que algo deve ser executado

/*
    do {
        execução
    }while(condição de parada)
*/
// FOR/IN

const notas = [5.5, 7.8, 8.9]
// for in devolve o indice e não os valores

for(let i in notas){
    console.log(i, notas[i])
}
// Usando com Objeto/dicionário

const pessoa = {nome: 'Divino', sobrenome: 'Luiz', idade: '24'}

for(let chave in pessoa){
    console.log(`O/A ${chave}, ${pessoa[chave]}`)
}
// colocar let dentro do for, deixa a variável visível apenas para aquele bloco

// BREAK E CONTINUE


const num = [1, 2, 3, 4, 5, 6, 7, 8]
for(let i in num){
    if(i == 5){
        break
    }
    console.log(`${i} = ${num[i]}`)
}
// break não para o bloco em que está, mas sim o bloco mais próximo associado a ele, logo, o for

for(let j in num){
    if(j == 5){
        continue
    }
    console.log(`${j} = ${num[j]}`)
}
// continue para a repetição em que está, mas não o bloco inteiro
// nesse caso não será impresso somente o número associado ao índice 5

externo: for (a in num){
    for(b in num){
        if (a == 2 && b == 3) break externo
        console.log(`${a}, ${b}`)
    }
}
// externo é o que se chama de rótulo
// o break para o bloco mais próximo, dessa forma ele pararia o segundo for, mas não primeiro
// para parar o primeiro, é necessário fazer um rótulo apontando o lugar que o break deve parar
// NÃO USAR BREAK E CONTINUE PARA CONTROLAR O CÓDIGO, ESSES MÉTODOS SÃO DESELEGANTES
// E DIFICULTAM PARA SE FAZER MANUTENÇÃO QUANDO NECESSÁRIO.