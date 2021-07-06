// Set -> conjunto
// Estrutura não indexada e que não aceita repetição

let set = new Set()
set.add(1)
set.add(2)
set.add(3)
set.add(4)
set.add(5)
set.add(1)
console.log(set)
console.log(set.size)
console.log(set.has(3))
set.delete(5)
console.log(set)

const array = [1, 2, 30, 4, 4]
set = new Set(array)
console.log(set)