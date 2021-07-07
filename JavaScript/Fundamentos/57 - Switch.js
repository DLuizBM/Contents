const imprimirNota = function(nota){
    switch(Math.floor(nota)){// Math.floor, arredonda o número para baixo
        case 10: // como 10 e 9 vão ter a mesma saída, é possível fazer nessa estrutura, para não precisar
        case 9:  // repetir código
            console.log("Aprovado - SS")
            break
        case 8: // mesma lógica das condições anteriores
        case 7:
            console.log("Aprovado - MS")
            break
        case 6: case 5: case 4: case 3: case 2: case 1: // é possível fazer dessa forma para condições repetidas
            console.log("Reprovado")
            break
        default: // valor padrão caso a entrada não esteja em nenhuma das condições anteriores
            console.log("Nota inválida")
    } 
}
imprimirNota(10)
imprimirNota(7.5)
imprimirNota(5)