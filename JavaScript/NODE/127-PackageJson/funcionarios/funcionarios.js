const url = 'http://files.cod3r.com.br/curso-js/funcionarios.json'
const axios = require('axios')
// axios é um client http, que faz requesições pra obter informações
// de algo que está remoto

// get obtém informação do servidor, quando a requisição retornar, chama o método the 
// quando é feita a requisição, obtém-se o conteúdo dessa url




axios.get(url).then(response => {
    var funcionarios = response.data
    // dentro do atributo data dessa resposta (response) eu tenho a lista de dicionários de funcionários
    

    // desafio, pegar a mulher chinesa com o menos salário

    const salarios = dados => dados.salario
    const getGenero = dados => dados.genero == 'F' && dados.pais == 'China'
    let mulherchinesa = funcionarios.filter(getGenero).map(salarios)
    console.log(mulherchinesa)
    console.log(mulherchinesa.length)


    const menorsalario = Math.min(...mulherchinesa)
    const menorSalario = dados => dados.salario == menorsalario
    const Mulher = funcionarios.filter(getGenero).filter(menorSalario)
    console.log(Mulher)
    


})

// Na aula 133, foi modificado o arquivo package.json
// adicionado o "start": "nodemon", para rodar no terminal: npm start
// e "dev": "nodemon", para rodar no terminal: npm run dev
// para criar a posta node_modules: npm init