const resultado = nota => nota >= 7 ? 'aprovado': 'reprovado'
// nota >= 7 ? 'aprovado': 'reprovado' -> aqui está o operador ternário
// se nota maior que 7 ?(verdadeiro) aprovado :(se não, falso) reprovado
// função arrow
console.log(resultado(7.5))