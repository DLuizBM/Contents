/* 
 -{} notação para a criação de objetos
 -objeto em JS é uma coleção com chave/valor, similar a dicionários no python
 -Não aceita chaves repetidas
  
*/

// Adicionando no dicionário

const prod1 = {nome: 'Divino', sobrenome: 'Luiz'}
// prod1 recebe o endereço de memória onde objeto está, ou seja, passagem por referência
// diferente de tipos primitivos(int, char ect), que a passagem é feita por valor

console.log(prod1)
prod1.profissão = 'engenheiro'
prod1["Idade"] = 24 // evitar essa notação
console.log(prod1)

const prod2 = {
    'Carro': 'Gol',
    'Ano': 2008 ,
    'Potência': {
        Gasolina: '72 cv',
        Etanol:{
                Puro: '81 cv',
                Misturado: '78cv'
        }
    }
}
// É possível colocar objetos dentro de objetos, funções dentro de objetos 
// É possível definir a chave com 'Carro' ou simplesmente o nome -> Carro
console.log(prod2)