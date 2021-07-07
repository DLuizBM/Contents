// para ler arquivos, deve-se usar o módulo interno file system

const fs = require('fs')
// fazendo a referência do módulo file system (fs)

const caminho = __dirname + '/arquivo.json'
// __dirname -> diretório atual; constante que está presente em todos os diretórios e arquivos do node

// leitura de forma síncrona
// faz toda a leitura do arquivo para só depois responder à requisição
// não recomendado para arquivos grandes, requisições em bancos de dados, requisição remota
// pois trava o event loop

const conteudo = fs.readFileSync(caminho, 'utf-8')
// 'utf-8' -> é o encode e como deve ser lido
console.log(conteudo)


// Assíncrono

fs.readFile(caminho, 'utf-8', (err, conteudo) => {
    const config = JSON.parse(conteudo)
    console.log(`${config.db.host}`)
    // posso escolher os atributos do objeto que quero trabalhar
})

// para ler direto um json: executado de forma síncrona
const config = require('./arquivo.json')
console.log(config.db)

// lendo uma pasta

fs.readdir(__dirname, (err, arquivos) =>{
    console.log(arquivos)
})