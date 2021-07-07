// Map é uma estrutura parecida com o Objeto
// possui chave e valor
// a chave não pode se repetir

const tecnologias = new Map()
tecnologias.set('react', {framework: false})
// reac = chave, {framework: false} = valor
tecnologias.set('angular', {framework: true})
console.log(tecnologias.get('react'))

const chaves = new Map([
    [function(){}, 'Função'],
    [{}, 'objeto'],
    [123, 'número']
])

chaves.forEach((ch, vl) => {
    console.log(ch, vl)
})

console.log(chaves.has(123))
// função has veifica se aquela chave está presente