const alunos = [
    {nome:'João', nota:7.2, bolsista: false},
    {nome:'Maria', nota:9.2 , bolsista: true},
    {nome:'Pedro', nota:9.8, bolsista: false},
    {nome:'Ana', nota:9.8, bolsista: false},
]

let bolsa = alunos.map(dic => dic.bolsista).reduce((bolsa, nbolsa) => Boolean(bolsa * nbolsa))
console.log(bolsa)
let algum = alunos.map(dic => dic.bolsista).reduce(function(bolsa, nbolsa){
    if((bolsa||nbolsa) == true){
        return true
    }else{
        return false
    }
}) 
console.log(algum)