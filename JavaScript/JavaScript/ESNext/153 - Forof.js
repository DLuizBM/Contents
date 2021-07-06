// Laço for que itera em cima de valores
// for in itera em cima de indices

const array = [10, 20, 30]

for(let i in array){
    console.log(i)
}

for(let i of array){
    console.log(i)
}

const obj = {
    nome: 'Luiza',
    idade: 25
}
for(let i of Object.values(obj)){
    console.log(i)
}

for(let [ch, vl] of Object.entries(obj)){
    console.log(ch, vl)
}