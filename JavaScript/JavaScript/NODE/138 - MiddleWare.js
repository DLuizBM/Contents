// Middleware pattern (chain of responsability) (cadeia de responsabilidade)

const passo1 = (context, next) => {
    // context: é o objeto que vai receber os dados
    // next: é a função que quando chamada vai disparar o próximo passo na cadeia
    context.valor1 = 'mid1'
    next()
}

const passo2 = (context, next) => {
    context.valor2 = 'mid2'
    next()
}

const passo3 = context => context.valor3 = 'mid3'


// ...middleware: recebe um conjunto de funções middleware, junta tudo dentro de um array
const exec = (context, ...middleware) => {
    const execPasso = indice => { // indice pega cada elemento do array middleware
        middleware && indice < middleware.length &&
            middleware[indice](context, () => execPasso(indice + 1))

        // virifica se middleware não é falso e se o índice é menor do que o tamanho do array
        // && no final significa que se todas as condições forem satisfeitas, deve-se executar
        // a próxima linha.
        // middleware[indice] -> como se trata de um array de funções, será executada a função daquele índice
        // ex: a função passo1 está no índice 0
        // (context, () => execPasso(indice + 1)): a função recebe 2 parâmetros, context e next
        // context = {}, vindo da linha 42 e next é () => execPasso(indice + 1), sendo essa uma recursividade
        
        // Fazendo o passo acima com if

        //if (middleware != false && indice < middleware.length){
            //middleware[indice](context, () => execPasso(indice + 1))
        //}

    } 
    execPasso(0) // da o início na função
}

const context = {}
exec(context, passo1, passo2, passo3)
console.log(context)