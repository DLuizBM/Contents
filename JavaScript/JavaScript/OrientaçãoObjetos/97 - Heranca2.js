// Cadeia de protótipo (prototype chain)
Object.prototype.attr0 = '0'
const avo = {attr1: 'a'}
const pai = {__proto__:avo, attr2: 'b', attr3: 'd'}
// para referenciar a herança deve-se usar __proto__:objetoquevaiserherdado
const filho = {__proto__: pai, attr3: 'c'}

// procurando na cadeia de protótipos
console.log(filho.attr1)
// filho não tem atributo1, vai procurar no pai, mas pai não tem, vai procurar no avo. Avo tem e retorna esse atributo
console.log(filho.attr4)
// saída: undefined
// vai procurar na cadeia de protótipos e no Object.prototype, como Object.prototype não tem
// retorna undefined 
console.log(filho.attr0)
// Nem filho, nem pai, nem avo têm esse atributo, porém Object.prototype foi definido
// como avo aponta para Object.prototype, Object.prototype retorna '0'

console.log(filho.attr3)
// saida: c e não d-> sempre procura o atributo mais perto de onde está chamando

const carro = {
    velAtual: 0,
    velMax: 200,
    aceleraMais(delta){
        if(this.velAtual + delta <= this.velMax){
            this.velAtual += delta
        }else{
            this.velAtual = this.velMax
        }
    },
    status(){
        return `${this.velAtual}km/h de ${this.velMax}km/h`
    }
}

const ferrari = {
    modelo: 'f40',
    velMax: 324, // shadowing -> sombreamento de atributo, após estabelcer a relação entre objeto e protótipo
}                // a velMax passa a ser 324

const volvo = {
    modelo: 'v40',
    status(){
        return `${this.modelo}: ${super.status()}`
        // this.modelo -> modelo do objeto atual
        // sobreescrevendo o método status do protótipo, usa-se a função 'super'  
    }
}

// Estabelecendo uma relação entre objeto e protótipo
Object.setPrototypeOf(ferrari, carro)
Object.setPrototypeOf(volvo, carro)

console.log(ferrari)
console.log(volvo)

console.log(volvo.status())
ferrari.aceleraMais(230)
console.log(ferrari.status())

