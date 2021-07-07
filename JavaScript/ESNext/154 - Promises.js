// A promise funciona de forma assíncrona
// onde após uma tarefa ser executada a promise é lançada
// resolve é quando a promise é aceita, aceita apenas um parâmetro
// reject é quando a promise é rejeitada

// se aceita vai para a função 'then', para ser executada

function falarDepois(segundos, frase){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(frase)
            // resolve executa a .then com o 'frase'
        }, segundos * 1000);
        // promise vai ser executada depois de se passarem os segundos determinados
    })
}
falarDepois(3, 'Olá mundo ')
        .then(frase => frase.concat('da programação!!'))
        .then(outraFrase => console.log(outraFrase))



function FalarDepois(segundos, frase){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            reject(frase)
        }, segundos * 1000);
    })
}

FalarDepois(1, 'OLÁ MUNDO ')
    .then(frase => frase.concat('da programação!!'))
    .then(outraFrase => console.log(outraFrase))
    .catch(e => console.log('Ops: Algo deu errado! :('))
// .cath é para fazer o tratamento de erros
//http://files.cod3r.com.br/curso-js/turmaA.json