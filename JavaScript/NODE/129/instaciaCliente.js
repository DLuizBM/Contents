const contadorA = require('./instanciaunica')
const contadorB = require('./instanciaunica')

const contadorC = require('./instaciaNova')()
const contadorD = require('./instaciaNova')()
// require('./instaciaNova') retorna uma função, () é necessário para retorna o objeto da função


contadorA.inc()
contadorA.inc()
console.log(contadorB.valor)
// saída: 3 -> como o node faz o cache por padrão 
// contado A e B, não são independentes, por isso contador B assume valor 3, mesmo não sendo chamado
// se o objeto já tiver sido criado, retorna sempre a mesma instância

contadorC.inc()
contadorC.inc()
console.log(contadorC.valor) // 3
console.log(contadorD.valor) // 1
// saídas diferentes, pois a função factory sempre retorna um novo objeto
// dessa forma, contador C e D são independentes