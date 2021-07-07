/*const objeto = {
    _id: 1,
    get id(){
        return this._id++
    }
}

let array = []
for(let i=0; i < 3; i++){
    array.push(objeto.id)
}
console.log(array)


function soma(num, callback){
    callback(num + '!!!')
}

soma('turma A', num => {
    console.log(num + 'blablabla')
})



const array = [ [1,2], [2], [3], [4]]

console.log(array) // [ [ 1, 2 ], [ 2 ], [ 3 ], [ 4 ] ]
console.log(...array) // [ 1, 2 ] [ 2 ] [ 3 ] [ 4 ]
console.log([].concat(...array)) // [ 1, 2, 2, 3, 4 ]
// o método concat tira tudo de dentro dos parênteses 
// o array [] vazio é importante para se ter um array para iterar

const frase = [['olá mundo'], [1, [2], 3]]
let novafrase = []
console.log(''.concat(frase))
// olá mundo,1,2,3
// o método concat tira tudo de dentro dos parênteses 


const array = [1, 2, 4]

array.forEach((e) => {
    console.log(e)
})

*/

lista = [20, 30, 40, 12]

const muda = lista.filter(num => num <= 20 )
console.log(muda)