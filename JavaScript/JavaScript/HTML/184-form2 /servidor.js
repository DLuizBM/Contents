const port = 3003
const express = require('express')
const app = express()
const bodyParser = require('body-parser')

app.use(bodyParser.urlencoded({extended: true}))

/*
app.post('/formulario', (req, res, next) =>{
    console.log(req.body)
    res.send('Dados formulário enviados com sucesso!!')
})
*/

app.post('/formulario/:id', (req, res, next) =>{
    console.log(req.params.id)
    console.log(req.body)
    res.send('Formulário alterado!')
})

app.get('/formulario', (req, res, next) =>{
    console.log(req.query)
    // mudar para GET o método em form.html
    //Quando o método é get, os dados não vem no body e sim na query string
    res.send('Dados obtidos com sucesso!!')
})
app.listen(port)