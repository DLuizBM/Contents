// JSON é um formato de dados, texto
const obj = {a: 1, b: 2, c: 3, soma(){return a + b + c}}
console.log(JSON.stringify(obj))
// obj para JSOn
// a função será excluída, pois o json só transfere dados e não execução

console.log(JSON.parse('{"a": 1, "b": 2, "c": 3}'))
// JSON para objeto
// para ser JSON deve-se ter os atributos entre "", e tudo envolvido em '', se sair desse padrão
// não é JSON

console.log(JSON.parse('{"a": 1, "b": "string", "c": true, "d": [], "e": {}}'))
