const http = require('http')

const getTurma = (letra) => {
    url = `http://files.cod3r.com.br/curso-js/turma${letra}.json`
    return new Promise((resolve, reject) => {
        http.get(url, res => {
            let resultado = ''

            res.on('data', dados => {
                // os dados não chegam todos de uma vez
                //  a variável resultado, vai sendo compondo à medida que os dados vão chegando
                resultado += dados
            })

            res.on('end', () => {
                try {
                    resolve(JSON.parse(resultado))
                }catch(e) {
                    // 'e' vai capturar a mensagem de erro.
                    reject(e)
                }
            })
        })
    })
} 

// Com essa função, posso passar promises em cadeia e quando todas forem resolvidas
// Aí serão chamadas as cadeias dos métodos then
Promise.all([getTurma('A'), getTurma('B'), getTurma('C')])
        .then(alunos => [].concat(...alunos))
        .then(alunos => alunos.map(aluno => aluno.nome))
        .then(nomes => console.log(nomes))
        .catch(e => console.log(e.message))
