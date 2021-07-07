const fs = require('fs')

const produto = {
    nome: 'celular',
    preco: 2400,
}

fs.writeFile(__dirname + '/arquivoGerado.json', JSON.stringify(produto), err => {
    console.log(err || 'Arquivo Salvo!!')
})

// JSON.stringify -> permite transformar um objeto em JS para uma string Json