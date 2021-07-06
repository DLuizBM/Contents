const _ = require('lodash')
// '_' convenção para referenciar a biblioteca lodash
// ('lodash'), para fazer a busca do arquivo index dentro da pasta
setInterval(() => console.log(_.random(1, 100)), 2000) 
// função random do lodash