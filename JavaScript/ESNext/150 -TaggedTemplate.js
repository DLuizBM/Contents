const array = [10, 20, 30, 40]
array.forEach((valor, indice) => console.log(valor, indice))

let teste = true
teste = (teste == false) ? 1 : 3
console.log(teste)

const array2 = []
array2.push(1, 10)
array2.push(2, 20)
array2.push(3, 30)
array2.push(4, 40, 400), 
console.log(array2)

function real(partes, ...valores){
    console.log(partes)
    console.log(valores)
    let resultado = []
    valores.forEach((valor, indice) => {
        valor = isNaN(valor) ? valor : `R$:${valor}`
        resultado.push(partes[indice], valor)
    })
    console.log(resultado.join('')) 
}

const preco = 29.9
const precoParcela = 11
real`1X de ${preco} ou 3X de ${precoParcela}.`