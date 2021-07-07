// configurando o Express

const porta = 3003

const express = require('express')
const app = express()
// instanciando o express

const bodyParser = require('body-parser')

app.use(bodyParser.urlencoded({extended: true})) //urlencoded: é uma função middleware
// qualquer requisição feita no express, vai passar por esse middleware
// essa função faz um parser transformando em objeto

// importando o "Banco de Dados"
const bancoDeDados = require('./bancoDeDados')

// '/produtos' é a url
app.get('/produtos', (req, res, next) => { 
    res.send(bancoDeDados.getProdutos())
    next()
    // usando o next para ir para a próxima função get
})

// fazendo uma requisição em cima de produtos, e como resposta uma função middleware
app.get('/produtos/:id', (req, res, next) => { 
    res.send(bancoDeDados.getProduto(req.params.id))
    // a função send envia uma resposta, que vai ser convertido para json
    // os parâmetros vem da requisição e não da resposta
    // o parâmetro vem diretamente da url
    // ex:http://localhost:3003/produtos/1 
    // tenho exatamente o produto com id = 1
    // req.params é o local onde coloco os parâmetros da url
})

app.post('/produtos', (req, res, next) => {
    const produto = bancoDeDados.salvarProduto({
        nome: req.body.nome,
        preco: req.body.preco,
    })
    res.send(produto)
})

app.put('/produtos/:id', (req, res, next) =>{
    const produto = bancoDeDados.salvarProduto({
        id: req.params.id,
        nome: req.body.nome,
        preco:req.body.preco
    })
    res.send(produto)
})

app.delete('/produtos/:id', (req, res, next) =>{
    const produto = bancoDeDados.deletarProduto(req.params.id)
    res.send(produto)
    // manda como resposta o que acabou de excluir
})

app.listen(porta, () => {
    console.log(`Servidor executando na porta ${porta}.`)
})