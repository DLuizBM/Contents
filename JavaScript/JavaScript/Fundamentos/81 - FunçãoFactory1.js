// Função factory é uma função que retorna um objeto

function Pessoa(nomes, telefones, enderecos=undefined){
    return{
        nome: nomes,
        telefone: telefones,
        endereco: enderecos,
    }
}

console.log(Pessoa('Hamilton', '555-5555'))
console.log(Pessoa('Alonso', '555-5555'))
console.log(Pessoa('Senna', '333-3333', 'São Paulo'))