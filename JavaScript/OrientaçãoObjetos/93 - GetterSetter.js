// JS não tem atributos privados
// Há uma convenção para indicar que tal atributo deve ser acessado ou modificado como atributo
// privado. Coloca-se um underline à frente do atributo, como no exemplo a seguir:

const sequencia = {
    _valor: 2, // convenção, lembrando que não impede que ele seja alterado,
     // porém deve-se respeitar e usar get e set para trabalhar com o atributo
    get valor() {
        return this._valor
    },
    set valor(valor) {
        if(valor > this._valor){
            this._valor += valor
        }
    }
}
sequencia.valor = 6 //apesar de get e set possuírem o mesmo nome(valor) entende que está atribuindo no set
console.log(sequencia.valor) // como não está atribuindo, entende que é o set
// o ideal é colocar para o get e set nomes diferentes
