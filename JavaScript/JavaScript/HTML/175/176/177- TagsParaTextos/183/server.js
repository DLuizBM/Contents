const express = require('express')
// importando o express
const app = express()
// instanciando o express e associando a variável app
const bodyParser = require('body-parser')
// importando badyparser. Quando os dados do formulário são submetidos, o body-parser faz um 
// parser no corpo da requisição, parser no corpo do request, pega esses dados e joga dentro 
// do request.body. Quando se acessa request.body, tem acesso a todos os dados do formulário
app.use(bodyParser.urlencoded({extended: true}))

//'/usuarios: url em que vai abir a página com a mensagem parabéns'
app.post('/usuarios', (req, res) => {
    console.log(req.body)
    res.send('Parabéns')
})
app.listen(3003)

// Para funciona deve-se rodar o http-server em /Conteúdo_Java_Script/HTML/175/176/177- TagsParaTextos
// e rodar node server.js para servir 