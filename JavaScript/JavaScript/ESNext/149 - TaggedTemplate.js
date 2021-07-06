
// Tagged template serve para passar template string para funções

function tag(valores, ...string){
    console.log(valores)
    console.log(string)
    // vai pegar apenas ${nome} e ${idade}
    return 'Outra string'
}
const nome = 'Gui'
const idade = '22'
console.log(tag`O ${nome} tem ${idade} anos.`)