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


// O objetivo é transformar um código que assíncrono em algo parecido com síncrono
// simplifica o código assíncrono
let ObterAlunos = async() => {
    const ta = await getTurma('A')
    const tb = await getTurma('B')
    const tc = await getTurma('C')
    return [].concat(ta, tb, tc)
    // retorna um objeto async function
}

ObterAlunos()
    .then(alunos => alunos.map(a => a.nome))
    .then(nomes => console.log(nomes))
